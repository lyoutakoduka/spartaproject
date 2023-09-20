#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spartaproject.script.execute.script_version import (version_from_string,
                                                         version_to_string)


def test_string() -> None:
    EXPECTED: str = '0.0.0'
    assert EXPECTED == version_to_string([0, 0, 0])


def test_number() -> None:
    EXPECTED: Ints = [0, 0, 0]
    assert EXPECTED == version_from_string('0.0.0')


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_string()
    test_number()
    return True
