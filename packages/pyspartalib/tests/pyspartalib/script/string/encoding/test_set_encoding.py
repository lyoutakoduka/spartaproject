#!/usr/bin/env python

"""Test module to encode string by specific character encoding."""

from pyspartalib.context.type_context import Type
from pyspartalib.script.string.encoding.set_encoding import set_encoding


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _compare_encoding(expected: bytes, result: bytes) -> None:
    assert expected == result


def _get_input() -> str:
    return "\u3042"


def test_utf() -> None:
    """Test to encode string by default character encoding."""
    expected: bytes = b"\xe3\x81\x82"

    _difference_error(set_encoding(_get_input()), expected)


def test_sjis() -> None:
    """Test to encode string by specific character encoding."""
    expected: bytes = b"\x82\xa0"

    _difference_error(
        set_encoding(_get_input(), encoding="shift_jis"),
        expected,
    )
