#!/usr/bin/env python

"""Test module to execute CLI (Command Line Interface) script on subprocess."""

from pathlib import Path

from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.directory.current.set_current import SetCurrent
from pyspartalib.script.directory.working.working_directory import (
    WorkingDirectory,
)
from pyspartalib.script.error.error_raise import (
    ErrorDifference,
    ErrorLength,
    ErrorNoExists,
)
from pyspartalib.script.shell.execute_command import ExecuteCommand


class _TestShare(
    ErrorLength,
    ErrorNoExists,
    ErrorDifference,
    WorkingDirectory,
):
    def _get_match(self) -> str:
        return "share"

    def _get_pwd(self) -> Strs:
        return ["pwd"]

    def _error_length(self, result: Strs) -> str:
        self.error_length(result, 1, self._get_match())
        return result[0]

    def _error_no_exists(self, path: Path) -> Path:
        self.error_no_exists(path, self._get_match())
        return path

    def get_single_path(self, result: Strs) -> Path:
        return self._error_no_exists(Path(self._error_length(result)))

    def set_current(self, function: Func) -> None:
        with SetCurrent(self.get_working_root()):
            function()


class TestSingle(_TestShare):
    def _get_current(self) -> Strs:
        return list(ExecuteCommand().execute_single(self._get_pwd()))

    def _get_result(self) -> Path:
        return self.get_single_path(self._get_current())

    def _inside_current(self) -> None:
        self.error_difference(
            self._get_result(),
            self.get_working_root(),
            "single",
        )

    def _individual_test(self) -> bool:
        self.set_current(self._inside_current)

        return True

    def test_single(self) -> None:
        """Test to execute generic script.

        Suppose that the test environment of Windows
            can execute simple Linux commands.
        """
        self.inside_working(self._individual_test)


class TestMultiple(_TestShare):
    def _initialize_root(self, move_root: Path) -> None:
        self._move_root: Path = move_root

    def _get_cd(self, expected: Path) -> Strs:
        return ["cd", expected.as_posix()]

    def _move_and_get(self, expected: Path) -> Strs:
        return list(
            ExecuteCommand().execute_multiple(
                [self._get_cd(expected), self._get_pwd()],
            ),
        )

    def _get_result(self, move_root: Path) -> Path:
        return self.get_single_path(self._move_and_get(move_root))

    def _inside_current(self, move_root: Path) -> None:
        self.error_difference(
            self._get_result(move_root),
            move_root,
            "multiple",
        )

    def _create_move_root(self) -> None:
        self._initialize_root(
            create_directory(Path(self.get_working_root(), "move")),
        )

    def _hide_arguments(self, move_root: Path) -> Func:
        return lambda: self._inside_current(move_root)

    def _individual_test(self) -> bool:
        self.set_current(self._hide_arguments(self._create_move_root()))

        return True

    def test_multiple(self) -> None:
        """Test to execute generic script which is multiple lines.

        Suppose that the test environment of Windows
            can execute simple Linux commands.
        """
        self.inside_working(self._individual_test)
