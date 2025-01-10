#!/usr/bin/env python

"""Test module to get statistics about file."""

from collections.abc import Sized
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.type_context import Type
from pyspartalib.script.file.text.export_file import text_export
from pyspartalib.script.path.status.get_statistic import (
    get_file_size,
    get_file_size_array,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _length_error(result: Sized, expected: int) -> None:
    if len(result) == expected:
        raise ValueError


def _get_texts() -> Strs:
    return ["first", "second", "third"]


def _get_expected_counts() -> Ints:
    return [len(text) for text in _get_texts()]


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_single() -> None:
    """Test to get file size."""
    text: str = "test"

    def individual_test(temporary_root: Path) -> None:
        _length_error(
            text,
            get_file_size(
                text_export(Path(temporary_root, "temporary.txt"), text),
            ),
        )

    _inside_temporary_directory(individual_test)


def test_array() -> None:
    """Test to get list of file size."""
    expected: Ints = _get_expected_counts()

    def individual_test(temporary_root: Path) -> None:
        result: Ints = get_file_size_array(
            [
                text_export(Path(temporary_root, text + ".txt"), text)
                for text in _get_texts()
            ],
        )
        _difference_error(result, expected)

    _inside_temporary_directory(individual_test)
