#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.execute.execute_command import execute_command


def test_current() -> None:
    result: Strs = execute_command(["pwd"])
    if 1 != len(result):
        assert False

    current: Path = Path(result[0])

    assert current.exists()
    assert current == Path.cwd()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_current()
    return True
