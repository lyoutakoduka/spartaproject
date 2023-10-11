#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to execute CLI (Command Line Interface) script on subprocess."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.path.modify.get_current import get_current
from pyspartaproj.script.shell.execute_command import execute_command


def test_current() -> None:
    """Test to execute generic script.

    Suppose that the test environment of Windows
        can execute simple Linux commands.
    """
    result: Strs = list(execute_command(["pwd"]))

    if 1 != len(result):
        fail()

    current: Path = Path(result[0])

    assert current.exists()
    assert current == get_current()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_current()
    return True
