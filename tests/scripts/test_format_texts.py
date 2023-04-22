#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

from scripts.format_texts import format_indent


_Strs = List[str]


def shared_compare(expected: _Strs, input: str) -> None:
    assert '\n'.join(expected) == format_indent(input)


def test_stdout() -> None:
    INPUT: str = """
        Hallo!
    """
    EXPECTED: _Strs = [
        "Hallo!",
        "",
    ]
    assert '\n'.join(EXPECTED) == format_indent(INPUT, stdout=True)


def test_vertical() -> None:
    INPUT: str = """
    　\t
        Hallo!
    　\n
    """
    EXPECTED: _Strs = [
        "Hallo!",
    ]
    shared_compare(EXPECTED, INPUT)


def test_horizontal() -> None:
    INPUT: str = """
    \t　    Hallo!    　\n
    """
    EXPECTED: _Strs = [
        "Hallo!",
    ]
    shared_compare(EXPECTED, INPUT)


def test_indent() -> None:
    INPUT: str = """
            Hallo!
        Hallo!
                Hallo!
    """
    EXPECTED: _Strs = [
        "    Hallo!",
        "Hallo!",
        "        Hallo!",
    ]
    shared_compare(EXPECTED, INPUT)


def test_inner() -> None:
    INPUT: str = """
        Hallo!    Hallo!


        Hallo!    Hallo!
    """
    EXPECTED: _Strs = [
        "Hallo!    Hallo!",
        "",
        "",
        "Hallo!    Hallo!",
    ]
    shared_compare(EXPECTED, INPUT)


def main() -> bool:
    test_stdout()
    test_vertical()
    test_horizontal()
    test_indent()
    test_inner()
    return True
