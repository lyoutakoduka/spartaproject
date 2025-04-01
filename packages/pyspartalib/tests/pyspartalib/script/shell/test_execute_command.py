#!/usr/bin/env python

"""Test module for executing specific CLI script on a subprocess.

Note that the simple Linux commands (cd, pwd) should be installed
    before execute the test on Windows environment.
"""

from pathlib import Path

from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.default.string_context import StrGene, Strs, Strs2
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.directory.current.set_current import SetCurrent
from pyspartalib.script.directory.working.working_directory import (
    WorkingDirectory,
)
from pyspartalib.script.error.error_catch import ErrorCatch
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

    def initialize_instance(self, instance: ExecuteCommand) -> None:
        self._instance = instance

    def create_instance(self) -> None:
        self.initialize_instance(ExecuteCommand())

    def get_instance(self) -> ExecuteCommand:
        return self._instance

    def get_single_path(self, result: Strs) -> Path:
        return self._error_no_exists(Path(self._error_length(result)))

    def set_current(self, function: Func) -> None:
        with SetCurrent(self.get_working_root()):
            function()

    def evaluate(self, generator: StrGene) -> Strs:
        return list(generator)


class TestSingle(_TestShare):
    """Test class to execute the specific single line CLI script."""

    def _get_current(self) -> Strs:
        return self.evaluate(
            self.get_instance().execute_single(self._get_pwd()),
        )

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
        """Test to execute the specific single line CLI script."""
        self.create_instance()
        self.inside_working(self._individual_test)


class TestMultiple(_TestShare):
    """Test class to execute the specific multi-line CLI script."""

    def _initialize_root(self, move_root: Path) -> None:
        self._move_root: Path = move_root

    def _get_cd(self) -> Strs:
        return ["cd", self._move_root.as_posix()]

    def _get_commands(self) -> Strs2:
        return [self._get_cd(), self._get_pwd()]

    def _move_and_get(self) -> Strs:
        return self.evaluate(
            self.get_instance().execute_multiple(self._get_commands()),
        )

    def _get_result(self) -> Path:
        return self.get_single_path(self._move_and_get())

    def _inside_current(self) -> None:
        self.error_difference(
            self._get_result(),
            self._move_root,
            "multiple",
        )

    def _create_move_root(self) -> None:
        self._initialize_root(
            create_directory(Path(self.get_working_root(), "move")),
        )

    def _individual_test(self) -> bool:
        self._create_move_root()
        self.set_current(self._inside_current)

        return True

    def test_multiple(self) -> None:
        """Test to execute the specific multi-line CLI script."""
        self.create_instance()
        self.inside_working(self._individual_test)


class TestNone(_TestShare, ErrorCatch):
    """Test class to raise the error forcibly and catch it."""

    def _get_command(self) -> Strs:
        return ["ls"]

    def _error_none(self) -> None:
        self.evaluate(self.get_instance().execute_single(self._get_command()))

    def _create_execute(self) -> ExecuteCommand:
        return ExecuteCommand(error_types=["none"])

    def test_none(self) -> None:
        """Test to raise the error forcibly and catch it."""
        self.initialize_instance(self._create_execute())
        self.catch_value(self._error_none, "process")
