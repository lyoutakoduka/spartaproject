#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to execute python code on server you can use ssh connection."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.safe.safe_copy import SafeCopy
from pyspartaproj.script.server.local.execute_server import ExecuteServer


def _is_connect(server: ExecuteServer) -> None:
    assert server.connect()


def _copy_resource(name: Path, destination_path: Path) -> None:
    SafeCopy().copy(get_resource(local_path=name), destination_path)


def _execute_python(name: Path, server: ExecuteServer) -> Strs | None:
    _is_connect(server)

    destination_path: Path = Path(server.get_working_root(), name)
    _copy_resource(name, destination_path)

    return server.execute(destination_path)


def _expected_result(name: Path) -> Strs:
    identifier: str = name.stem
    return [identifier + str(i) for i in range(3)]


def _filter_execute_error(name: Path, server: ExecuteServer) -> Strs:
    result: Strs | None = _execute_python(name, server)

    if result is None:
        fail()

    return result


def _common_test(name: Path, server: ExecuteServer) -> None:
    assert _expected_result(name) == _filter_execute_error(name, server)


def _version_test(name: Path, server: ExecuteServer, expected: str) -> None:
    assert expected == _get_version_number(_filter_execute_error(name, server))


def _get_version_number(result: Strs) -> str:
    return result[0].split(" ")[0]


def _get_server() -> ExecuteServer:
    return ExecuteServer(jst=True)


def _get_server_version(version: str) -> ExecuteServer:
    return ExecuteServer(jst=True, version=version)


def test_file() -> None:
    """Test to execute Python module that is single file."""
    name: Path = Path("file.py")
    server: ExecuteServer = _get_server()

    _common_test(name, server)


def test_directory() -> None:
    """Test to execute Python module including directory."""
    name: Path = Path("directory")
    server: ExecuteServer = _get_server()

    _common_test(name, server)


def test_version() -> None:
    """Test to execute selected version of Python interpreter."""
    name: Path = Path("version.py")
    expected: str = "3.10.11"
    server: ExecuteServer = _get_server_version(expected)

    _version_test(name, server, expected)


def test_error() -> None:
    """Test to catch and print error of Python code on server."""
    name: Path = Path("error.py")
    server: ExecuteServer = ExecuteServer()

    with raises(ValueError):
        _execute_python(name, server)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_directory()
    test_version()
    return True
