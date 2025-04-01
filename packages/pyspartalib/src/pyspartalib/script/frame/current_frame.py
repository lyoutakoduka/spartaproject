#!/usr/bin/env python

"""Module to get the current frame from the stack frames."""

from inspect import FrameInfo, currentframe, getouterframes
from pathlib import Path
from types import FrameType

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.error.error_force import ErrorForce
from pyspartalib.script.error.error_raise import ErrorNone, ErrorRaise
from pyspartalib.script.frame.context.frame_context import (
    StackFrame,
    StackFrames,
)
from pyspartalib.script.path.modify.current.get_relative import get_relative


class CurrentFrame(ErrorForce, ErrorNone, ErrorRaise):
    """Class to get the current frame from the stack frames."""

    def __initialize_super_class(self, error_types: Strs | None) -> None:
        ErrorForce.__init__(self, error_types)

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

    def _select_fail_condition(self) -> FrameType | None:
        return None if self.send_signal("none") else currentframe()

    def _confirm_result(self) -> FrameType:
        return self.error_none_walrus(self._select_fail_condition(), "frame")

    def _find_stack_frame_error(self) -> StackFrames:
        if (current_frame := self._select_fail_condition()) is None:
            self.error_value("frame")

        return self._get_stack_frames(current_frame)

    def _to_relative_path(self, frame: StackFrame) -> StackFrame:
        frame["file"] = get_relative(frame["file"])
        return frame

    def _select_frame(self, offset: int, frames: StackFrames) -> StackFrame:
        return frames[3 + offset]

    def get_frame(self, offset: int = 0) -> StackFrame:
        """Get the current frame from the stack frames.

        Args:
            offset (int, optional): Defaults to 0.
                Index offset of the stack frames based on the current frame.

        Returns:
            StackFrame: Selected the current frame.

        """
        return self._to_relative_path(
            self._select_frame(offset, self._find_stack_frame_error()),
        )

    def __init__(self, error_types: Strs | None = None) -> None:
        """Initialize the class variables.

        Args:
            force_fail (bool, optional): Defaults to False.
                If true, retrieving the stack frames will fail.

        """
        self.__initialize_super_class(error_types)
