#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert text to specific type."""

from pyspartaproj.script.string.convert_type import convert_integer


def test_number() -> None:
    """Test to convert text to type "integer"."""
    assert 1 == convert_integer("0001")


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_number()
    return True
