#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from platform import python_version
from sys import executable

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.script.execute.script_version import (
    execute_version,
    get_version_name,
    version_from_string,
    version_to_string,
)


def test_string() -> None:
    EXPECTED: str = "0.0.0"
    assert EXPECTED == version_to_string([0, 0, 0])


def test_number() -> None:
    EXPECTED: Ints = [0, 0, 0]
    assert EXPECTED == version_from_string("0.0.0")


def test_name() -> None:
    EXPECTED: str = "Python-0.0.0"
    assert EXPECTED == get_version_name([0, 0, 0])


def test_version() -> None:
    assert execute_version(Path(executable)) == version_from_string(
        python_version()
    )


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_string()
    test_number()
    test_name()
    test_version()
    return True
