#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute Python depends on OS."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.shell.execute_python import (
    execute_python,
    get_interpreter_path,
)


def test_command() -> None:
    results: Strs = list(
        execute_python(
            [Path(Path(__file__).parent, "resource", "version.py").as_posix()]
        )
    )

    if 1 == len(results):
        interpreter_path: Path = Path(results[0])
        assert interpreter_path == get_interpreter_path()
    else:
        fail()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_command()
    return True
