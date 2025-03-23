#!/usr/bin/env python

"""Module to get stack frames information."""

from inspect import FrameInfo, currentframe, getouterframes
from pathlib import Path
from types import FrameType

from pyspartalib.script.error.error_raise import ErrorRaise
from pyspartalib.script.frame.context.frame_context import (
    StackFrame,
    StackFrames,
)
from pyspartalib.script.path.modify.current.get_relative import get_relative


class CurrentFrame(ErrorRaise):
    def __initialize_variables(self, force_fail: bool) -> None:
        self._force_fail: bool = force_fail

    def _get_stack_frame(self, outer_frame: FrameInfo) -> StackFrame:
        return {
            "file": Path(outer_frame.filename),
            "function": outer_frame.function,
            "line": outer_frame.lineno,
        }

    def _get_stack_frames(self, current_frame: FrameType) -> StackFrames:
        return [
            self._get_stack_frame(outer_frame)
            for outer_frame in getouterframes(current_frame)
        ]

    def _find_stack_frame_error(self) -> StackFrames:
        if current_frame := currentframe():
            return self._get_stack_frames(current_frame)

        return self.error_value("frame")

    def _to_relative_path(self, frame: StackFrame) -> StackFrame:
        frame["file"] = get_relative(frame["file"])
        return frame

    def get_frame(self, offset: int = 0) -> StackFrame:
        """Get current frame information in stack frames.

        Args:
            offset (int, optional): Defaults to 0.
                Index offset of stack frames based on current frame.

        Returns:
            StackFrame: Selected current frame information.

        """
        return self._to_relative_path(
            self._find_stack_frame_error()[2 + offset],
        )

    def __init__(self, force_fail: bool = False) -> None:
        self.__initialize_variables(force_fail)
