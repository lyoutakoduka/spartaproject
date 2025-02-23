#!/usr/bin/env python

"""Module to get stack frames information."""

from inspect import FrameInfo, currentframe, getouterframes
from pathlib import Path
from types import FrameType
from typing import NoReturn

from pyspartalib.script.frame.context.frame_context import (
    StackFrame,
    StackFrames,
)
from pyspartalib.script.path.modify.current.get_relative import get_relative


def _raise_error(message: str) -> NoReturn:
    raise ValueError(message)


def _get_stack_frame(outer_frame: FrameInfo) -> StackFrame:
    return {
        "file": Path(outer_frame.filename),
        "function": outer_frame.function,
        "line": outer_frame.lineno,
    }


def _get_stack_frames(current_frame: FrameType) -> StackFrames:
    return [
        _get_stack_frame(outer_frame)
        for outer_frame in getouterframes(current_frame)
    ]


def _find_stack_frame_error() -> StackFrames:
    if current_frame := currentframe():
        return _get_stack_frames(current_frame)

    _raise_error("frame")


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
    return _to_relative_path(_find_stack_frame_error()[2 + offset])
