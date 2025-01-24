#! /usr/bin/env python

"""Test module to get stack frames information."""

from pathlib import Path

from pyspartalib.context.type_context import Type
from pyspartalib.script.frame.stack_frame import StackFrame, current_frame
from pyspartalib.script.path.modify.current.get_relative import get_relative


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_file_expected() -> Path:
    return get_relative(Path(__file__))


def _get_frame_current() -> StackFrame:
    return {
        "file": _get_file_expected(),
        "function": "test_current",
        "line": 23,
    }


def _get_frame_offset() -> StackFrame:
    return {
        "file": _get_file_expected(),
        "function": "test_offset",
        "line": 37,
    }


def test_current() -> None:
    """Test to get current frame information in stack frames."""
    _difference_error(current_frame(), _get_frame_current())


def test_offset() -> None:
    """Test to get current frame information with index offset."""

    def inside_function() -> None:
        _difference_error(current_frame(offset=1), _get_frame_offset())

    inside_function()
