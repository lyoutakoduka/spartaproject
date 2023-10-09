#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.file.text.export_file import byte_export, text_export


def _common_test(text_path: Path, count: int) -> None:
    assert text_path.stat().st_size == count


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        text_path: Path = Path(temporary_path, "temporary.txt")
        function(text_path)


def test_text() -> None:
    source_text: str = "test"

    def individual_test(text_path: Path) -> None:
        _common_test(text_export(text_path, source_text), len(source_text))

    _inside_temporary_directory(individual_test)


def test_byte() -> None:
    source_byte: bytes = b"test"

    def individual_test(text_path: Path) -> None:
        _common_test(byte_export(text_path, source_byte), len(source_byte))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_text()
    test_byte()
    return True
