#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from pytest import raises

from context.default.string_context import Strs
from script.path.safe.safe_copy import SafeCopy
from script.server.execute_server import ExecuteServer


def _execute_python(is_file: bool, type: str) -> Strs | None:
    server: ExecuteServer = ExecuteServer()

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


def _common_test(is_file: bool, type: str) -> bool:
    if result := _execute_python(is_file, type):
        return result == _expected_result(type)

    return False


def test_file() -> None:
    type: str = 'file'
    assert _common_test(True, type)


def test_directory() -> None:
    type: str = 'directory'
    assert _common_test(False, type)


def test_error() -> None:
    type: str = 'error'
    with raises(ValueError):
        _execute_python(True, type)


def main() -> bool:
    test_file()
    test_directory()
    return True
