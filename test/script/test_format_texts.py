#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spartaproject.context.default.string_context import Strs
from spartaproject.script.format_texts import format_indent


def shared_compare(expected: Strs, input: str, stdout: bool = False) -> None:
    assert '\n'.join(expected) == format_indent(input, stdout=stdout)


def test_stdout() -> None:
    INPUT: str = """
        Hallo!
    """
    EXPECTED: Strs = ["Hallo!", ""]
    shared_compare(EXPECTED, INPUT, stdout=True)


def test_vertical() -> None:
    INPUT: str = """
    　\t
        Hallo!
    　\n
    """
    EXPECTED: Strs = ["Hallo!"]
    shared_compare(EXPECTED, INPUT)


def test_horizontal() -> None:
    INPUT: str = """
    \t　    Hallo!    　\n
    """
    EXPECTED: Strs = ["Hallo!"]
    shared_compare(EXPECTED, INPUT)


def test_indent() -> None:
    INPUT: str = """
            Hallo!
        Hallo!
                Hallo!
    """
    EXPECTED: Strs = [
        "    Hallo!",
        "Hallo!",
        "        Hallo!"
    ]
    shared_compare(EXPECTED, INPUT)


def test_inner() -> None:
    INPUT: str = """
        Hallo!    Hallo!


        Hallo!    Hallo!
    """
    EXPECTED: Strs = [
        "Hallo!    Hallo!",
        "",
        "",
        "Hallo!    Hallo!"
    ]
    shared_compare(EXPECTED, INPUT)


def main() -> bool:
    test_stdout()
    test_vertical()
    test_horizontal()
    test_indent()
    test_inner()
    return True
