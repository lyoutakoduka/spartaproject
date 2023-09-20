#!/usr/bin/env python
# -*- coding: utf-8 -*-

from platform import python_version

from spartaproject.context.default.integer_context import Ints
from spartaproject.script.execute.script_version import (execute_version,
                                                         version_from_string,
                                                         version_to_string)


def test_string() -> None:
    EXPECTED: str = '0.0.0'
    assert EXPECTED == version_to_string([0, 0, 0])


def test_number() -> None:
    EXPECTED: Ints = [0, 0, 0]
    assert EXPECTED == version_from_string('0.0.0')


def test_version() -> None:
    assert execute_version() == version_from_string(python_version())


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_string()
    test_number()
    test_version()
    return True
