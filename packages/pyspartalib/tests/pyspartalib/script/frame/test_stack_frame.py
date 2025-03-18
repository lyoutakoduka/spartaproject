#! /usr/bin/env python

"""Test module to get stack frames information."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.frame.context.frame_context import StackFrame
from pyspartalib.script.frame.stack_frame import current_frame
from pyspartalib.script.path.modify.current.get_relative import get_relative


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


class _Share:
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


class TestCurrent(_Share):
    def _get_frame_current(self) -> StackFrame:
        return self.get_expected_frame("test_current", 40)

    def test_current(self) -> None:
        """Test to get current frame information in stack frames."""
        _difference_error(current_frame(), self._get_frame_current())  # Here


class TestOffset(_Share):
    def _get_frame_offset(self) -> StackFrame:
        return self.get_expected_frame("test_offset", 52)

    def _inside_function(self) -> None:
        _difference_error(current_frame(offset=1), self._get_frame_offset())

    def test_offset(self) -> None:
        """Test to get current frame from an offset stack frame."""
        self._inside_function()  # Here
