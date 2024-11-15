#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get stack frames information."""

import inspect
from pathlib import Path

from pyspartaproj.context.typed.builtin_context import StackFrame, StackFrames
from pyspartaproj.script.path.modify.current.get_relative import get_relative


def _get_stack_frames() -> StackFrames:
    stack_frames: StackFrames = []

    if current_frame := inspect.currentframe():
        for outer_frame in inspect.getouterframes(current_frame):
            stack_frame: StackFrame = {
                "file": Path(outer_frame.filename),
                "function": outer_frame.function,
                "line": outer_frame.lineno,
            }
            stack_frames += [stack_frame]

    return stack_frames


def _to_relative_path(frame: StackFrame) -> StackFrame:
    frame["file"] = get_relative(frame["file"])
    return frame


def current_frame(offset: int = 0) -> StackFrame:
    """Function to get current frame information in stack frames.

    Args:
        offset (int, optional): Defaults to 0.
            Index offset of stack frames based on current frame.

    Returns:
        StackFrame: Selected current frame information.
    """
    stack_frames: StackFrames = _get_stack_frames()
    return _to_relative_path(stack_frames[2 + offset])
