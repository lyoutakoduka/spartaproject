#!/usr/bin/env python

"""Test module to execute CLI (Command Line Interface) script on subprocess."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.path.modify.current.get_current import get_current
from pyspartalib.script.shell.execute_command import (
    execute_multiple,
    execute_single,
)
from tests.pyspartalib.interface.pytest import fail


def _get_current() -> Strs:
    return list(execute_single(["pwd"]))


def test_single() -> None:
    """Test to execute generic script.

    Suppose that the test environment of Windows
        can execute simple Linux commands.
    """
    result: Strs = _get_current()

    if len(result) != 1:
        fail()

    current: Path = Path(result[0])

    assert current.exists()
    assert current == get_current()


def test_multiple() -> None:
    """Test to execute generic script which is multiple lines.

    Suppose that the test environment of Windows
        can execute simple Linux commands.
    """
    with TemporaryDirectory() as temporary_directory:
        expected: Path = Path(temporary_directory)

        result: Strs = list(
            execute_multiple([["cd", expected.as_posix()], ["pwd"]]),
        )

        if len(result) != 1:
            fail()

        assert expected == Path(result[0])
