#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.file.archive.archive_format import (
    get_format,
    rename_format,
)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_format() -> str:
    return "zip"


def test_format() -> None:
    assert _get_format() == get_format()


def test_rename() -> None:
    def individual_test(temporary_root: Path) -> None:
        expected: Path = temporary_root.with_suffix("." + _get_format())
        assert expected == rename_format(temporary_root)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_format()
    test_rename()
    return True
