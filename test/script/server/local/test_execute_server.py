#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to execute python code on server you can use ssh connection."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.feature_flags import in_development
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.safe.safe_copy import SafeCopy
from pyspartaproj.script.server.local.execute_server import ExecuteServer


def _execute_python(name: str, server: ExecuteServer) -> Strs | None:
    assert server.connect()

    destination_path: Path = Path(server.create_local_working_space(), name)

    safe_copy = SafeCopy()
    safe_copy.copy(get_resource(local_path=Path(name)), destination_path)

    return server.execute(destination_path)


def _expected_result(name: str) -> Strs:
    identifier: str = Path(name).stem
    return [identifier + str(i) for i in range(3)]


def _filter_execute_error(name: str, server: ExecuteServer) -> Strs:
    result: Strs | None = _execute_python(name, server)

    if result is None:
        fail()

    return result


def _common_test(name: str, server: ExecuteServer) -> None:
    assert _expected_result(name) == _filter_execute_error(name, server)


def _version_test(name: str, server: ExecuteServer, expected: str) -> None:
    assert expected == _get_version_number(_filter_execute_error(name, server))


def _get_version_number(result: Strs) -> str:
    return result[0].split(" ")[0]


def _get_server() -> ExecuteServer:
    return ExecuteServer(jst=True)


def test_file() -> None:
    """Test to execute Python module that is single file."""
    name: str = "file.py"
    server: ExecuteServer = _get_server()

    _common_test(name, server)


def test_directory() -> None:
    """Test to execute Python module including directory."""
    name: str = "directory"
    server: ExecuteServer = _get_server()

    _common_test(name, server)


def test_path() -> None:
    """Test to execute selected version of Python interpreter."""
    name: str = "version.py"
    expected: str = "3.10.11"
    server: ExecuteServer = ExecuteServer(version=expected)

    if in_development():
        _version_test(name, server, expected)


def test_error() -> None:
    """Test to catch and print error of Python code on server."""
    name: str = "error.py"
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
    test_path()
    return True
