#!/usr/bin/env python

"""Test module to execute CLI (Command Line Interface) script on subprocess."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathFunc
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


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


class _TestShare(
    ErrorLength,
    ErrorNoExists,
    ErrorDifference,
    WorkingDirectory,
):
    def _get_match(self) -> str:
        return "share"

    def get_single_path(self, result: Strs) -> Path:
        self.error_length(result, 1, self._get_match())
        path: Path = Path(result[0])
        self.error_no_exists(path, self._get_match())
        return path


class TestSingle(_TestShare):
    def _get_current(self) -> Strs:
        return list(ExecuteCommand().execute_single(["pwd"]))

    def test_single(self) -> None:
        """Test to execute generic script.

        Suppose that the test environment of Windows
            can execute simple Linux commands.
        """

        def individual_test(temporary_root: Path) -> None:
            with SetCurrent(temporary_root):
                self.error_difference(
                    self.get_single_path(self._get_current()),
                    temporary_root,
                    "single",
                )

        _inside_temporary_directory(individual_test)


class TestMultiple(_TestShare):
    def _move_and_get(self, expected: Path) -> Strs:
        return list(
            ExecuteCommand().execute_multiple(
                [["cd", expected.as_posix()], ["pwd"]],
            ),
        )

    def test_multiple(self) -> None:
        """Test to execute generic script which is multiple lines.

        Suppose that the test environment of Windows
            can execute simple Linux commands.
        """

        def individual_test(temporary_root: Path) -> None:
            move_root: Path = create_directory(Path(temporary_root, "move"))

            with SetCurrent(temporary_root):
                self.error_difference(
                    self.get_single_path(self._move_and_get(move_root)),
                    move_root,
                    "multiple",
                )

        _inside_temporary_directory(individual_test)
