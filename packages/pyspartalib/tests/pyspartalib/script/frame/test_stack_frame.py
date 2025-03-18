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


class TestCurrent(_Share):
    def _get_frame_current(self) -> StackFrame:
        return {
            "file": self.get_file_expected(),
            "function": "test_current",
            "line": 40,
        }

    def test_current(self) -> None:
        """Test to get current frame information in stack frames."""
        _difference_error(current_frame(), self._get_frame_current())  # Here


class TestOffset(_Share):
    def _get_frame_offset(self) -> StackFrame:
        return {
            "file": self.get_file_expected(),
            "function": "test_offset",
            "line": 49,
        }

    def test_offset(self) -> None:
        """Test to get current frame from an offset stack frame."""

        def inside_function() -> None:
            _difference_error(
                current_frame(offset=1),
                self._get_frame_offset(),
            )

        inside_function()  # Here
