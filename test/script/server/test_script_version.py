#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from platform import python_version
from sys import executable

from pyspartaproj.script.server.script_version import (
    execute_version,
    get_version_name,
)


def test_name() -> None:
    expected: str = "Python-0.0.0"
    assert expected == get_version_name("0.0.0")


def test_version() -> None:
    assert python_version() == execute_version(Path(executable))


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_name()
    test_version()
    return True
