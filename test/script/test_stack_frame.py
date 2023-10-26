#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.stack_frame import StackFrame, current_frame


def _get_file_expected() -> Path:
    return get_relative(Path(__file__))


def test_current() -> None:
    expected: StackFrame = {
        "file": _get_file_expected(),
        "function": "test_current",
        "line": 20,
    }
    assert expected == current_frame()


def test_offset() -> None:
    expected: StackFrame = {
        "file": _get_file_expected(),
        "function": "test_offset",
        "line": 33,
    }

    def inside_function() -> None:
        assert expected == current_frame(offset=1)

    inside_function()


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: success if get to the end of function
    """
    test_current()
    test_offset()
    return True
