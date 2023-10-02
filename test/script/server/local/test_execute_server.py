#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pytest import raises

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.execute.script_version import version_from_string
from pyspartaproj.script.path.safe.safe_copy import SafeCopy
from pyspartaproj.script.server.local.execute_server import ExecuteServer


def _get_execute_source(name: str) -> Path:
    current: Path = Path(__file__)
    return Path(current.parents[1], "execute", name)


def _execute_python(name: str, server: ExecuteServer) -> Strs | None:
    assert server.connect()

    destination_path: Path = Path(server.get_working_space(), name)

    safe_copy = SafeCopy()
    safe_copy.copy(_get_execute_source(name), destination_path)

    return server.execute(destination_path)


def _expected_result(name: str) -> Strs:
    identifier: str = Path(name).stem
    return [identifier + str(i) for i in range(3)]


def _common_test(name: str, server: ExecuteServer) -> None:
    if result := _execute_python(name, server):
        assert _expected_result(name) == result
    else:
        assert False


def _version_test(name: str, server: ExecuteServer, expected: Ints) -> None:
    if result := _execute_python(name, server):
        assert expected == _get_version_number(result)
    else:
        assert False


def _get_version_number(result: Strs) -> Ints:
    version_text = result[0]
    texts: Strs = version_text.split(" ")

    return version_from_string(texts[0])


def test_file() -> None:
    name: str = "file.py"
    server: ExecuteServer = ExecuteServer()

    _common_test(name, server)


def test_directory() -> None:
    name: str = "directory"
    server: ExecuteServer = ExecuteServer()

    _common_test(name, server)


def test_version() -> None:
    name: str = "version.py"
    EXPECTED: Ints = [3, 10, 11]
    server: ExecuteServer = ExecuteServer(versions=EXPECTED)

    _version_test(name, server, EXPECTED)


def test_error() -> None:
    name: str = "error.py"
    server: ExecuteServer = ExecuteServer()

    with raises(ValueError):
        _execute_python(name, server)


def main() -> bool:
    test_file()
    test_directory()
    test_version()
    return True
