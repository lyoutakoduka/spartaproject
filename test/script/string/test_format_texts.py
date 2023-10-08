#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.format_texts import format_indent


def shared_compare(expected: Strs, input: str, stdout: bool = False) -> None:
    assert "\n".join(expected) == format_indent(input, stdout=stdout)


def test_stdout() -> None:
    input: str = """
        Hallo!
    """
    expected: Strs = ["Hallo!", ""]
    shared_compare(expected, input, stdout=True)


def test_vertical() -> None:
    input: str = """
    　\t
        Hallo!
    　\n
    """
    expected: Strs = ["Hallo!"]
    shared_compare(expected, input)


def test_horizontal() -> None:
    input: str = """
    \t　    Hallo!    　\n
    """
    expected: Strs = ["Hallo!"]
    shared_compare(expected, input)


def test_indent() -> None:
    input: str = """
            Hallo!
        Hallo!
                Hallo!
    """
    expected: Strs = ["    Hallo!", "Hallo!", "        Hallo!"]
    shared_compare(expected, input)


def test_inner() -> None:
    input: str = """
        Hallo!    Hallo!


        Hallo!    Hallo!
    """
    expected: Strs = ["Hallo!    Hallo!", "", "", "Hallo!    Hallo!"]
    shared_compare(expected, input)


def main() -> bool:
    test_stdout()
    test_vertical()
    test_horizontal()
    test_indent()
    test_inner()
    return True
