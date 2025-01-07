#!/usr/bin/env python

"""Test module to find character encoding from string automatically."""

from pyspartalib.context.type_context import Type
from pyspartalib.script.string.encoding.find_encoding import find_encoding
from pyspartalib.script.string.encoding.set_encoding import set_encoding


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _same_error(result: Type, expected: Type) -> None:
    if result == expected:
        raise ValueError


def _get_input() -> str:
    return chr(12354)


def _same_encoding(expected: str, result: bytes) -> None:
    _difference_error(find_encoding(result), expected)


def _not_same_encoding(expected: str, result: bytes) -> None:
    _same_error(find_encoding(result), expected)


def test_utf() -> None:
    """Test to find character encoding which is UTF-8."""
    _same_encoding("utf-8", set_encoding(_get_input()))


def test_sjis() -> None:
    """Test to find character encoding which is Shift JIS."""
    encoding: str = "shift-jis"
    _same_encoding(encoding, set_encoding(_get_input(), encoding=encoding))


def test_other() -> None:
    """Test to find character encoding which is others."""
    _not_same_encoding(
        "shift-jis",
        set_encoding(_get_input(), encoding="euc-jp"),
    )
