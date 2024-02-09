#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.format_texts import format_indent


def _common_test(expected: Strs, source: str, stdout: bool = False) -> None:
    assert "\n".join(expected) == format_indent(source, stdout=stdout)


def test_stdout() -> None:
    source: str = """
        Hallo!
    """
    expected: Strs = ["Hallo!", ""]
    _common_test(expected, source, stdout=True)


def test_vertical() -> None:
    source: str = """
    　\t
        Hallo!
    　\n
    """
    expected: Strs = ["Hallo!"]
    _common_test(expected, source)


def test_horizontal() -> None:
    source: str = """
    \t　    Hallo!    　\n
    """
    expected: Strs = ["Hallo!"]
    _common_test(expected, source)


def test_indent() -> None:
    source: str = """
            Hallo!
        Hallo!
                Hallo!
    """
    expected: Strs = ["    Hallo!", "Hallo!", "        Hallo!"]
    _common_test(expected, source)


def test_inner() -> None:
    source: str = """
        Hallo!    Hallo!


        Hallo!    Hallo!
    """
    expected: Strs = ["Hallo!    Hallo!", "", "", "Hallo!    Hallo!"]
    _common_test(expected, source)


def main() -> bool:
    test_stdout()
    test_vertical()
    test_horizontal()
    test_indent()
    test_inner()
    return True
