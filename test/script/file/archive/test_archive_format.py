#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get information of archive format."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.extension.path_context import PathFunc
from pyspartaproj.script.file.archive.archive_format import (
    get_format,
    rename_format,
)


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_format() -> str:
    return "zip"


def test_format() -> None:
    """Test to get information of archive format."""
    assert _get_format() == get_format()


def test_rename() -> None:
    """Test to add archive format to path you select."""

    def individual_test(temporary_root: Path) -> None:
        expected: Path = temporary_root.with_suffix("." + _get_format())
        assert expected == rename_format(temporary_root)

    _inside_temporary_directory(individual_test)
