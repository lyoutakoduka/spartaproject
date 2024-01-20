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


def test_array() -> None:
    paths: Paths = [_current_path, _unknown_path]
    expected: Bools = [True, False]

    assert bool_compare_array(expected, check_exists_array(paths))


def test_pair() -> None:
    paths: PathPair = {
        "R": _current_path,
        "G": _unknown_path,
        "B": _current_path.parent,
    }
    expected: BoolPair = {"R": True, "G": False, "B": True}

    assert bool_compare_pair(expected, check_exists_pair(paths))


def main() -> bool:
    test_array()
    test_pair()
    return True
