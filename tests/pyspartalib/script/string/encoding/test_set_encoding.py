#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to encode string by specific character encoding."""

from pyspartalib.script.string.encoding.set_encoding import set_encoding


def _compare_encoding(expected: bytes, result: bytes) -> None:
    assert expected == result


def _get_input() -> str:
    return "\u3042"


def test_utf() -> None:
    """Test to encode string by default character encoding."""
    expected: bytes = b"\xe3\x81\x82"

    _compare_encoding(expected, set_encoding(_get_input()))


def test_sjis() -> None:
    """Test to encode string by specific character encoding."""
    expected: bytes = b"\x82\xa0"

    _compare_encoding(
        expected, set_encoding(_get_input(), encoding="shift_jis")
    )
