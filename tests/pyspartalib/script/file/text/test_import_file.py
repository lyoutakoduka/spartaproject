#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to import text file."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.file.text.export_file import text_export
from pyspartalib.script.file.text.import_file import byte_import, text_import
from pyspartalib.script.string.encoding.set_decoding import set_decoding


def _common_test(result: str) -> None:
    assert "test" == result


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(text_export(Path(temporary_path, "temporary.txt"), "test"))


def test_byte() -> None:
    """Test to import binary file."""

    def individual_test(text_path: Path) -> None:
        _common_test(set_decoding(byte_import(text_path)))

    _inside_temporary_directory(individual_test)


def test_text() -> None:
    """Test to import text file."""

    def individual_test(text_path: Path) -> None:
        _common_test(text_import(text_path))

    _inside_temporary_directory(individual_test)
