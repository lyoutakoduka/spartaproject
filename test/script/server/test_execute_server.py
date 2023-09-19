#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pytest import raises
from spartaproject.context.default.integer_context import Ints
from spartaproject.context.default.string_context import Strs
from spartaproject.script.path.safe.safe_copy import SafeCopy
from spartaproject.script.server.execute_server import ExecuteServer


def _execute_python(type: str, server: ExecuteServer) -> Strs | None:
    assert server.connect()

    current: Path = Path(__file__)
    destination_path: Path = Path(server.get_working_space(), type)

    safe_copy = SafeCopy()
    safe_copy.copy(Path(current.parent, 'execute', type), destination_path)

    return server.execute(destination_path)


def _expected_result(type: str) -> Strs:
    identifier: str = Path(type).stem
    return [identifier + str(i) for i in range(3)]


def _common_test(type: str, server: ExecuteServer) -> bool:
    if result := _execute_python(type, server):
        assert result == _expected_result(type)
    else:
        assert False


def _get_version_number(result: Strs) -> Ints:
    version_text = result[0]
    texts: Strs = version_text.split(' ')
    text: str = texts[0]

    return [int(number) for number in text.split('.')]


def test_file() -> None:
    type: str = 'file.py'
    server: ExecuteServer = ExecuteServer()

    _common_test(type, server)


def test_directory() -> None:
    type: str = 'directory'
    server: ExecuteServer = ExecuteServer()

    _common_test(type, server)


def test_version() -> None:
    type: str = 'version.py'
    EXPECTED: Ints = [3, 11, 3]
    server: ExecuteServer = ExecuteServer(versions=EXPECTED)

    if result := _execute_python(type, server):
        assert EXPECTED == _get_version_number(result)


def test_error() -> None:
    type: str = 'error.py'
    server: ExecuteServer = ExecuteServer()

    with raises(ValueError):
        _execute_python(type, server)


def main() -> bool:
    test_file()
    test_directory()
    test_version()
    return True
