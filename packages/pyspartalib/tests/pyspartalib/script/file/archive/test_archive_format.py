#!/usr/bin/env python

"""Test module to get information of archive format."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.type_context import Type
from pyspartalib.script.file.archive.archive_format import (
    get_format,
    rename_format,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_format() -> str:
    return "zip"


def test_format() -> None:
    """Test to get information of archive format."""
    _difference_error(get_format(), _get_format())


def test_rename() -> None:
    """Test to add archive format to path you select."""

    def individual_test(temporary_root: Path) -> None:
        _difference_error(
            rename_format(temporary_root),
            temporary_root.with_suffix("." + _get_format()),
        )

    _inside_temporary_directory(individual_test)
