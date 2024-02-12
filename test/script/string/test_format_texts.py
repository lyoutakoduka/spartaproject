#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to remove white space at the beginning of a sentence."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.format_texts import format_indent


def _common_test(expected: Strs, source: str, stdout: bool = False) -> None:
    assert "\n".join(expected) == format_indent(source, stdout=stdout)


def test_stdout() -> None:
    """Test to remove white space at the beginning of a sentence."""
    source: str = """
        Hallo!
    """
    expected: Strs = ["Hallo!", ""]
    _common_test(expected, source, stdout=True)


def test_vertical() -> None:
    """Test to remove white space, tab character, and line break.

    Characters which should removed are placed to both ends of whole sentence.
    """
    source: str = """
    　\t
        Hallo!
    　\n
    """
    expected: Strs = ["Hallo!"]
    _common_test(expected, source)


def test_horizontal() -> None:
    """Test to remove white space, tab character, and line break.

    Characters which should removed are placed to both ends of one line text.
    """
    source: str = """
    \t　    Hallo!    　\n
    """
    expected: Strs = ["Hallo!"]
    _common_test(expected, source)


def test_indent() -> None:
    """Test to remove white space at the beginning of a sentence.

    Same count of white space are removed for all lines.
    """
    source: str = """
            Hallo!
        Hallo!
                Hallo!
    """
    expected: Strs = ["    Hallo!", "Hallo!", "        Hallo!"]
    _common_test(expected, source)


def test_inner() -> None:
    """Test to remove white space at the beginning of a sentence.

    Same count of white space are removed for all lines.
    But empty line is an exception.
    """
    source: str = """
        Hallo!    Hallo!


        Hallo!    Hallo!
    """
    expected: Strs = ["Hallo!    Hallo!", "", "", "Hallo!    Hallo!"]
    _common_test(expected, source)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_stdout()
    test_vertical()
    test_horizontal()
    test_indent()
    test_inner()
    return True
