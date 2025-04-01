#! /usr/bin/env python

"""Test module to get the current frame from the stack frames."""

from pathlib import Path

from pyspartalib.script.error.error_catch import ErrorCatch
from pyspartalib.script.error.error_raise import ErrorDifference
from pyspartalib.script.frame.context.frame_context import StackFrame
from pyspartalib.script.frame.current_frame import CurrentFrame
from pyspartalib.script.path.modify.current.get_relative import get_relative


class _TestShare(ErrorDifference):
    def get_file_expected(self) -> Path:
        return get_relative(Path(__file__).resolve())

    def get_expected_frame(
        self,
        function_name: str,
        line_number: int,
    ) -> StackFrame:
        return {
            "file": self.get_file_expected(),
            "function": function_name,
            "line": line_number,
        }


class TestCurrent(_TestShare):
    """Class to get the current frame from the stack frames."""

    def _get_result(self) -> StackFrame:
        return CurrentFrame().get_frame()

    def _get_expected(self) -> StackFrame:
        return self.get_expected_frame("_get_result", 34)

    def test_current(self) -> None:
        """Test to get the current frame from the stack frames."""
        self.error_difference(
            self._get_result(),
            self._get_expected(),
            "current",
        )


class TestOffset(_TestShare):
    """Class to get the current frame from the offset stack frame."""

    def _get_result(self) -> StackFrame:
        return CurrentFrame().get_frame(offset=1)

    def _get_expected(self) -> StackFrame:
        return self.get_expected_frame("test_offset", 60)

    def test_offset(self) -> None:
        """Test to get the current frame from the offset stack frame."""
        self.error_difference(
            self._get_result(),
            self._get_expected(),
            "offset",
        )


class TestError(_TestShare, ErrorCatch):
    """Class to get the current frame, but it fails."""

    def _initialize_instance(self, instance: CurrentFrame) -> None:
        self._instance = instance

    def _get_instance(self) -> CurrentFrame:
        return self._instance

    def _get_result(self) -> None:
        CurrentFrame(force_fail=True).get_frame()

    def test_error(self) -> None:
        """Test to get the current frame, but it fails."""
        self.catch_value(self._get_result, "frame")
