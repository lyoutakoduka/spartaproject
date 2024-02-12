#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to export text file."""

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


def test_byte() -> None:
    """Test to export binary file."""
    source_byte: bytes = b"test"

    def individual_test(text_path: Path) -> None:
        _common_test(byte_export(text_path, source_byte), len(source_byte))

    _inside_temporary_directory(individual_test)


def test_text() -> None:
    """Test to export text file."""
    source_text: str = "test"

    def individual_test(text_path: Path) -> None:
        _common_test(text_export(text_path, source_text), len(source_text))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_byte()
    test_text()
    return True
