#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute Python according to OS."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.shell.execute_python import (
    execute_python,
    get_interpreter_path,
)


def test_command() -> None:
    """Test to execute Python script that return version of interpreter."""
    results: Strs = list(
        execute_python([get_resource(["version.py"]).as_posix()])
    )

    if 1 == len(results):
        assert Path(results[0]) == get_interpreter_path()
    else:
        fail()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_command()
    return True
