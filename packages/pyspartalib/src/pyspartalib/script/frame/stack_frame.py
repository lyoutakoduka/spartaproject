#!/usr/bin/env python

"""Module to get stack frames information."""

import inspect
from inspect import FrameInfo
from pathlib import Path

from pyspartalib.script.path.modify.current.get_relative import get_relative

from .context.frame_context import StackFrame, StackFrames


def _get_stack_frame(outer_frame: FrameInfo) -> StackFrame:
    return {
        "file": Path(outer_frame.filename),
        "function": outer_frame.function,
        "line": outer_frame.lineno,
    }


def _get_stack_frames() -> StackFrames:
    if current_frame := inspect.currentframe():
        return [
            _get_stack_frame(outer_frame)
            for outer_frame in inspect.getouterframes(current_frame)
        ]

    raise ValueError


def _to_relative_path(frame: StackFrame) -> StackFrame:
    frame["file"] = get_relative(frame["file"])
    return frame


def current_frame(offset: int = 0) -> StackFrame:
    """Get current frame information in stack frames.

    Args:
        offset (int, optional): Defaults to 0.
            Index offset of stack frames based on current frame.

    Returns:
        StackFrame: Selected current frame information.

    """
    return _to_relative_path(_get_stack_frames()[2 + offset])
