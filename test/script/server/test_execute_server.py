#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pytest import raises
from spartaproject.context.default.integer_context import Ints
from spartaproject.context.default.string_context import Strs
from spartaproject.script.path.safe.safe_copy import SafeCopy
from spartaproject.script.server.execute_server import ExecuteServer


def _get_execute_source(name: str) -> Path:
    current: Path = Path(__file__)
    return Path(current.parent, 'execute', name)


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
        assert result == _expected_result(name)
    else:
        assert False


def _version_test(name: str, server: ExecuteServer, expected: Ints) -> None:
    if result := _execute_python(name, server):
        assert expected == _get_version_number(result)
    else:
        assert False


def _get_version_number(result: Strs) -> Ints:
    version_text = result[0]
    texts: Strs = version_text.split(' ')
    text: str = texts[0]

    return [int(number) for number in text.split('.')]


def test_file() -> None:
    name: str = 'file.py'
    server: ExecuteServer = ExecuteServer()

    _common_test(name, server)


def test_directory() -> None:
    name: str = 'directory'
    server: ExecuteServer = ExecuteServer()

    _common_test(name, server)


def test_version() -> None:
    name: str = 'version.py'
    EXPECTED: Ints = [3, 11, 3]
    server: ExecuteServer = ExecuteServer(versions=EXPECTED)

    _version_test(name, server, EXPECTED)


def test_error() -> None:
    name: str = 'error.py'
    server: ExecuteServer = ExecuteServer()

    with raises(ValueError):
        _execute_python(name, server)


def main() -> bool:
    test_file()
    test_directory()
    test_version()
    return True
