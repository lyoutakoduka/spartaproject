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
    """Class to get the current frame information from the stack frames."""

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

    def _current_frame(self) -> FrameType | None:
        if self._force_fail:
            return None

        return currentframe()

    def _find_stack_frame_error(self) -> StackFrames:
        if (current_frame := self._current_frame()) is None:
            self.error_value("frame")

        return self._get_stack_frames(current_frame)

    def _to_relative_path(self, frame: StackFrame) -> StackFrame:
        frame["file"] = get_relative(frame["file"])
        return frame

    def get_frame(self, offset: int = 0) -> StackFrame:
        """Get the current frame information from the stack frames.

        Args:
            offset (int, optional): Defaults to 0.
                Index offset of the stack frames based on the current frame.

        Returns:
            StackFrame: Selected the current frame information.

        """
        return self._to_relative_path(
            self._find_stack_frame_error()[2 + offset],
        )

    def __init__(self, force_fail: bool = False) -> None:
        """Initialize the class variables.

        Args:
            force_fail (bool, optional): Defaults to False.
                If true, retrieving the stack frames will fail.

        """
        self.__initialize_variables(force_fail)
