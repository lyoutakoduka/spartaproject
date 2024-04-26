#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working directory shared in class."""

from pathlib import Path

from pyspartaproj.script.directory.work_space import WorkSpace
from pyspartaproj.script.path.modify.get_relative import is_relative


def _compare_directory(work_space: WorkSpace) -> None:
    sub_root: Path = work_space.create_sub_directory("test")

    assert sub_root.exists()
    assert is_relative(sub_root, root_path=work_space.get_working_root())


def test_root() -> None:
    """Test to check existing of temporary working directory."""
    work_space = WorkSpace()
    work_space_root: Path = work_space.get_working_root()
    assert work_space_root.exists()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_root()
    return True
