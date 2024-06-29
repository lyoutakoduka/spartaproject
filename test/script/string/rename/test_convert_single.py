#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert multiple byte characters.

There are converted to single byte same characters in Ascii table.
"""

from pyspartaproj.script.string.rename.convert_single import ConvertSingle


def _common_test(expected: str, text: str) -> None:
    assert expected == ConvertSingle().convert(text)


def test_error() -> None:
    """Test to convert unsupported character."""
    text: str = "\u3042"
    expected: str = text

    _common_test(expected, text)


def test_single() -> None:
    """Test to convert multiple byte character."""
    text: str = "\uff21"
    expected: str = "A"

    _common_test(expected, text)


def test_array() -> None:
    """Test to convert list of multiple byte character."""
    text: str = "\uff34\uff25\uff33\uff34"
    expected: str = "TEST"

    _common_test(expected, text)


def test_small() -> None:
    """Test to convert small letter."""
    text: str = "\uff41"
    expected: str = "a"

    _common_test(expected, text)


def test_number() -> None:
    """Test to convert number character."""
    text: str = "\uff10"
    expected: str = "0"

    _common_test(expected, text)


def test_other() -> None:
    """Test to convert character other than alphabet and number."""
    text: str = "\uff5e"
    expected: str = "~"

    _common_test(expected, text)
