#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get statistics about file."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.file.text.export_file import text_export
from pyspartaproj.script.path.status.get_statistic import get_file_size


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
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


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_single()
    return True
