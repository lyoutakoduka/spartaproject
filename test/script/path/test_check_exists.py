#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to check existing of files or directories."""

from pathlib import Path

from pyspartaproj.context.default.bool_context import BoolPair, Bools
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.script.bool.compare_value import (
    bool_compare_array,
    bool_compare_pair,
)
from pyspartaproj.script.path.check_exists import (
    check_exists_array,
    check_exists_pair,
)
from pyspartaproj.script.stack_frame import current_frame


def _get_current_file() -> Path:
    return current_frame()["file"]


def _get_unknown_file(path: Path) -> Path:
    return path.with_name("unknown.py")


def test_array() -> None:
    """Test to check existing of list of file or directory."""
    current_file: Path = _get_current_file()
    paths: Paths = [current_file, _get_unknown_file(current_file)]
    expected: Bools = [True, False]

    assert bool_compare_array(expected, check_exists_array(paths))


def test_pair() -> None:
    """Test to check existing of directory of file or directory."""
    current_file: Path = _get_current_file()
    paths: PathPair = {
        "R": current_file,
        "G": _get_unknown_file(current_file),
        "B": current_file.parent,
    }
    expected: BoolPair = {"R": True, "G": False, "B": True}

    assert bool_compare_pair(expected, check_exists_pair(paths))


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_array()
    test_pair()
    return True
