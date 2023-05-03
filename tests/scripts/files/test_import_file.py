#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.files.export_file import text_export
from scripts.files.import_file import text_import, byte_import

_INPUT: str = 'test'


def _common_test(result: str) -> None:
    assert _INPUT == result


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        text_path: Path = Path(tmp_path, 'tmp.txt')
        text_export(text_path, _INPUT)
        func(text_path)


def test_text() -> None:
    def individual_test(text_path: Path) -> None:
        _common_test(text_import(text_path))

    _inside_tmp_directory(individual_test)


def test_byte() -> None:
    def individual_test(text_path: Path) -> None:
        result: bytes = byte_import(text_path)
        _common_test(result.decode('utf-8'))

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_text()
    test_byte()
    return True
