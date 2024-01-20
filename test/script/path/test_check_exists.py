#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

_current_path: Path = Path(__file__)
_unknown_path: Path = _current_path.with_name("unknown.py")


def _get_current_file() -> Path:
    return current_frame()["file"]


def _get_unknown_file() -> Path:
    return _get_current_file().with_name("unknown.py")


def test_array() -> None:
    current_file: Path = _get_current_file()
    unknown_path: Path = _get_unknown_file()

    paths: Paths = [current_file, unknown_path]
    expected: Bools = [True, False]

    assert bool_compare_array(expected, check_exists_array(paths))


def test_pair() -> None:
    current_file: Path = _get_current_file()
    unknown_path: Path = _get_unknown_file()

    paths: PathPair = {
        "R": current_file,
        "G": unknown_path,
        "B": current_file.parent,
    }
    expected: BoolPair = {"R": True, "G": False, "B": True}

    assert bool_compare_pair(expected, check_exists_pair(paths))


def main() -> bool:
    test_array()
    test_pair()
    return True
