#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.file.text.export_file import text_export
from pyspartaproj.script.file.text.import_file import byte_import, text_import

_input: str = "test"


def _common_test(result: str) -> None:
    assert _input == result


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(text_export(Path(temporary_path, "temporary.txt"), _input))


def test_text() -> None:
    def individual_test(text_path: Path) -> None:
        _common_test(text_import(text_path))

    _inside_temporary_directory(individual_test)


def test_byte() -> None:
    def individual_test(text_path: Path) -> None:
        result: bytes = byte_import(text_path)
        _common_test(result.decode())

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_text()
    test_byte()
    return True
