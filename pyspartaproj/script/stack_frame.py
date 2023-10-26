#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
from pathlib import Path
from typing import List, TypedDict

from pyspartaproj.script.path.modify.get_relative import get_relative


class StackFrame(TypedDict):
    file: Path
    function: str
    line: int


_StackFrames = List[StackFrame]


def _get_stack_frames() -> _StackFrames:
    stack_frames: _StackFrames = []

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


def current_frame() -> StackFrame:
    stack_frames: _StackFrames = _get_stack_frames()
    return _to_relative_path(stack_frames[2])
