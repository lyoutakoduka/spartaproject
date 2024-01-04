#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get datetime about selected file or directory."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch


def _common_test(path: Path) -> None:
    assert 1 == len(
        set([get_file_epoch(path, access=status) for status in [False, True]])
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to get latest datetime about file you select."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(create_temporary_file(temporary_root))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to get latest datetime about directory you select."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(create_directory(Path(temporary_root, "temporary")))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_directory()
    return True
