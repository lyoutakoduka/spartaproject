#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working directory shared in class."""

from pathlib import Path

from pyspartaproj.script.directory.create_directory_temporary import WorkSpace


class TemporaryWorkSpace(WorkSpace):
    pass


def test_create() -> None:
    """Test to check existing of temporary working directory."""
    work_space = TemporaryWorkSpace()
    work_space_root: Path = work_space.get_root()
    assert work_space_root.exists()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_create()
    return True
