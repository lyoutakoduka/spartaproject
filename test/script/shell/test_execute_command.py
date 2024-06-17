#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to execute CLI (Command Line Interface) script on subprocess."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.path.modify.get_current import get_current
from pyspartaproj.script.shell.execute_command import (
    execute_multiple,
    execute_single,
)


def test_single() -> None:
    """Test to execute generic script.

    Suppose that the test environment of Windows
        can execute simple Linux commands.
    """
    result: Strs = list(execute_single(["pwd"]))

    if 1 != len(result):
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
            execute_multiple([["cd", expected.as_posix()], ["pwd"]])
        )

        if 1 != len(result):
            fail()

        assert expected == Path(result[0])
