#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working directory shared in class."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.directory.work_space import WorkSpace
from pyspartaproj.script.path.modify.get_relative import is_relative


def _compare_directory(work_space: WorkSpace) -> None:
    sub_root: Path = work_space.create_sub_directory("test")

    assert sub_root.exists()
    assert is_relative(sub_root, root_path=work_space.get_working_root())


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_root() -> None:
    """Test to check existing of temporary working directory."""
    work_space = WorkSpace()
    work_space_root: Path = work_space.get_working_root()
    assert work_space_root.exists()


def test_directory() -> None:
    """Test for path of temporary working space you specified."""

    def individual_test(temporary_root: Path) -> None:
        _compare_directory(WorkSpace(working_root=temporary_root))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_root()
    test_directory()
    return True
