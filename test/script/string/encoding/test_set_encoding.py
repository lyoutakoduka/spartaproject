#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to encode string by specific character encoding."""

from pyspartaproj.script.string.encoding.set_encoding import set_encoding


def _compare_encoding(expected: bytes, result: bytes) -> None:
    assert expected == result


def test_utf() -> None:
    """Test to encode string by default character encoding."""
    source_text: str = "\u3042"
    expected: bytes = b"\xe3\x81\x82"

    _compare_encoding(expected, set_encoding(source_text))


def test_sjis() -> None:
    """Test to encode string by specific character encoding."""
    source_text: str = "\u3042"
    expected: bytes = b"\x82\xa0"

    _compare_encoding(
        expected, set_encoding(source_text, encoding="shift_jis")
    )
