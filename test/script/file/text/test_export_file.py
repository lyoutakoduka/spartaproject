#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to export text file."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.extension.path_context import PathFunc
from pyspartaproj.script.file.text.export_file import byte_export, text_export
from pyspartaproj.script.path.status.get_statistic import get_file_size


def _common_test(text_path: Path, count: int) -> None:
    assert get_file_size(text_path) == count


def _inside_temporary_directory(function: PathFunc) -> None:
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
