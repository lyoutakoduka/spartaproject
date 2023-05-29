#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from script.files.export_file import text_export, byte_export


def _common_test(text_path: Path, count: int) -> None:
    assert text_path.stat().st_size == count


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        text_path: Path = Path(temporary_path, 'temporary.txt')
        function(text_path)


def test_text() -> None:
    INPUT: str = 'test'

    def individual_test(text_path: Path) -> None:
        _common_test(text_export(text_path, INPUT), len(INPUT))

    _inside_temporary_directory(individual_test)


def test_byte() -> None:
    INPUT: bytes = b'test'

    def individual_test(text_path: Path) -> None:
        _common_test(byte_export(text_path, INPUT), len(INPUT))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_text()
    test_byte()
    return True
