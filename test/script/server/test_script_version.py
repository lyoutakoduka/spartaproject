#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from platform import python_version
from sys import executable

from pyspartaproj.script.server.script_version import (
    get_interpreter_version,
    get_version_name,
)


def test_name() -> None:
    assert "Python-0.0.0" == get_version_name("0.0.0")


def test_version() -> None:
    assert python_version() == get_interpreter_version(Path(executable))


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_name()
    test_version()
    return True
