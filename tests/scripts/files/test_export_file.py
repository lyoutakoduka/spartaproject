#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.files.export_file import text_export, byte_export


def _common_test(text_path: Path, count: int) -> None:
    assert text_path.stat().st_size == count


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        text_path: Path = Path(tmp_path, 'tmp.txt')
        func(text_path)


def test_all() -> None:
    INPUT: str = 'test'

    def individual_test(text_path: Path) -> None:
        text_export(text_path, INPUT)
        _common_test(text_path, len(INPUT))

    _inside_tmp_directory(individual_test)


def test_byte() -> None:
    INPUT: bytes = b'test'

    def individual_test(text_path: Path) -> None:
        byte_export(text_path, INPUT)
        _common_test(text_path, len(INPUT))

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_all()
    test_byte()
    return True
