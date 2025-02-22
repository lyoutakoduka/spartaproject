#!/usr/bin/env python

"""Test module to execute CLI (Command Line Interface) script on subprocess."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.directory.current.get_current import get_current
from pyspartalib.script.directory.current.set_current import SetCurrent
from pyspartalib.script.shell.execute_command import (
    execute_multiple,
    execute_single,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _no_exists_error(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError

    return path


def _get_single_path(result: Strs) -> Path:
    _difference_error(len(result), 1)
    return _no_exists_error(Path(result[0]))


def _get_current() -> Strs:
    return list(execute_single(["pwd"]))


def _move_and_get(expected: Path) -> Strs:
    return list(
        execute_multiple([["cd", expected.as_posix()], ["pwd"]]),
    )


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_single() -> None:
    """Test to execute generic script.

    Suppose that the test environment of Windows
        can execute simple Linux commands.
    """

    def individual_test(temporary_root: Path) -> None:
        with SetCurrent(temporary_root):
            _difference_error(_get_single_path(_get_current()), temporary_root)

    _inside_temporary_directory(individual_test)


def test_multiple() -> None:
    """Test to execute generic script which is multiple lines.

    Suppose that the test environment of Windows
        can execute simple Linux commands.
    """

    def individual_test(temporary_root: Path) -> None:
        move_root: Path = create_directory(Path(temporary_root, "move"))

        with SetCurrent(temporary_root):
            _difference_error(
                _get_single_path(_move_and_get(move_root)),
                move_root,
            )

    _inside_temporary_directory(individual_test)
