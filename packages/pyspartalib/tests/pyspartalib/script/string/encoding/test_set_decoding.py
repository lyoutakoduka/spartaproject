#!/usr/bin/env python

"""Test module to decode byte data by specific character encoding."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.string.encoding.set_decoding import set_decoding


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _compare_decoding(result: str) -> None:
    _difference_error(result, "\u3042")


def test_utf() -> None:
    """Test to decode byte data by default character encoding."""
    _compare_decoding(set_decoding(b"\xe3\x81\x82"))


def test_sjis() -> None:
    """Test to decode byte data by specific character encoding."""
    _compare_decoding(set_decoding(b"\x82\xa0", encoding="shift_jis"))
