#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert multiple byte characters to single byte."""

from pyspartaproj.script.string.translate_single import translate_single


def _common_test(expected: str, text: str) -> None:
    assert expected == translate_single(text)


def test_error() -> None:
    """Test to convert unsupported character."""
    text: str = "\u3042"
    expected: str = text

    _common_test(expected, text)


def test_single() -> None:
    """Test to convert multiple byte character to single byte character."""
    text: str = "\uff21"
    expected: str = "A"

    _common_test(expected, text)


def test_array() -> None:
    """Test to convert multiple byte characters to single byte characters."""
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
