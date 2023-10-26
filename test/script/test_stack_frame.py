#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.stack_frame import StackFrame, current_frame


def test_current() -> None:
    expected: StackFrame = {
        "file": get_relative(Path(__file__)),
        "function": "test_current",
        "line": 16,
    }
    assert expected == current_frame()


def test_offset() -> None:
    expected: StackFrame = {
        "file": get_relative(Path(__file__)),
        "function": "test_offset",
        "line": 29,
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
