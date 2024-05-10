#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create empty temporary file as json format."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to create empty temporary file as json format."""

    def individual_test(temporary_root: Path) -> None:
        expected: Path = Path(temporary_root, "temporary.json")
        file_path: Path = create_temporary_file(temporary_root)

        assert expected == file_path
        assert file_path.exists()

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    return True
