#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from context.default.string_context import Strs
from script.server.execute_server import ExecuteServer


def _execute_python(is_file: bool, type: str) -> Strs | None:
    server: ExecuteServer = ExecuteServer()

    if not server.connect():
        return None

    current: Path = Path(__file__)

    return server.execute(
        Path(current.parent, 'execute', type + '.py' if is_file else type)
    )


def _expected_result(type: str) -> Strs:
    return [type + str(i) for i in range(3)]


def _common_test(is_file: bool, type: str) -> bool:
    if result := _execute_python(is_file, type):
        return result == _expected_result(type)

    return False


def test_directory() -> None:
    type: str = 'directory'
    assert _common_test(False, type)


def test_file() -> None:
    type: str = 'file'
    assert _common_test(True, type)


def main() -> bool:
    test_directory()
    test_file()
    return True
