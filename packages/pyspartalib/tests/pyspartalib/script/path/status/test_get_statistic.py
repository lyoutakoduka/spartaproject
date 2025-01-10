#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get statistics about file."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.file.text.export_file import text_export
from pyspartalib.script.path.status.get_statistic import (
    get_file_size,
    get_file_size_array,
)


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_single() -> None:
    """Test to get file size."""
    text: str = "test"

    def individual_test(temporary_root: Path) -> None:
        assert len(text) == get_file_size(
            text_export(Path(temporary_root, "temporary.txt"), text)
        )

    _inside_temporary_directory(individual_test)


def test_array() -> None:
    """Test to get list of file size."""
    texts: Strs = ["first", "second", "third"]
    expected: Ints = [len(text) for text in texts]

    def individual_test(temporary_root: Path) -> None:
        result: Ints = get_file_size_array(
            [
                text_export(Path(temporary_root, text + ".txt"), text)
                for text in texts
            ]
        )

        assert expected == result

    _inside_temporary_directory(individual_test)
