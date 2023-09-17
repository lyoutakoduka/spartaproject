#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from context.default.integer_context import Ints
from context.default.string_context import Strs
from pytest import raises
from script.path.safe.safe_copy import SafeCopy
from script.server.execute_server import ExecuteServer


def _execute_python(
    is_file: bool, type: str, server: ExecuteServer
) -> Strs | None:
    if not server.connect():
        return None

    current: Path = Path(__file__)
    upload_target: str = type + '.py' if is_file else type
    destination_path: Path = Path(server.get_working_space(), upload_target)

    safe_copy = SafeCopy()
    safe_copy.copy(
        Path(current.parent, 'execute', upload_target), destination_path
    )

    return server.execute(destination_path)


def _expected_result(type: str) -> Strs:
    return [type + str(i) for i in range(3)]


def _common_test(is_file: bool, type: str, server: ExecuteServer) -> bool:
    if result := _execute_python(is_file, type, server):
        return result == _expected_result(type)

    return False


def _get_version_number(result: Strs) -> Ints:
    version_text = result[0]
    texts: Strs = version_text.split(' ')
    text: str = texts[0]

    return [int(number) for number in text.split('.')]


def test_file() -> None:
    type: str = 'file'
    server: ExecuteServer = ExecuteServer()

    assert _common_test(True, type, server)


def test_directory() -> None:
    type: str = 'directory'
    server: ExecuteServer = ExecuteServer()

    assert _common_test(False, type, server)


def test_version() -> None:
    type: str = 'version'
    EXPECTED: Ints = [3, 11, 3]
    server: ExecuteServer = ExecuteServer(versions=EXPECTED)

    if result := _execute_python(True, type, server):
        assert EXPECTED == _get_version_number(result)


def test_error() -> None:
    type: str = 'error'
    server: ExecuteServer = ExecuteServer()

    with raises(ValueError):
        _execute_python(True, type, server)


def main() -> bool:
    test_file()
    test_directory()
    test_version()
    return True
