#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test module to create all parent directories of the path you select."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.directory.create_parent import create_parent


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_directory() -> None:
    """Test to create all parent directories of the path you select."""

    def individual_test(temporary_root: Path) -> None:
        expected: Path = Path(temporary_root, "parent")
        parent_path: Path = create_parent(Path(expected, "temporary.json"))

        assert expected == parent_path
        assert parent_path.exists()

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_directory()
    return True
