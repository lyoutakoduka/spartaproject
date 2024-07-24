#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to find character encoding from string automatically."""

from pyspartaproj.script.string.encoding.find_encoding import find_encoding
from pyspartaproj.script.string.encoding.set_encoding import set_encoding


def _get_input() -> str:
    return chr(12354)


def _same_encoding(expected: str, result: bytes) -> None:
    assert expected == find_encoding(result)


def _not_same_encoding(expected: str, result: bytes) -> None:
    assert expected != find_encoding(result)


def _compare_encoding(encoding: str) -> None:
    _same_encoding(encoding, set_encoding(_get_input(), encoding=encoding))


def test_utf() -> None:
    """Test to find character encoding which is UTF-8."""
    _same_encoding("utf-8", set_encoding(_get_input()))


def test_sjis() -> None:
    """Test to find character encoding which is Shift JIS."""
    _compare_encoding("shift-jis")


def test_other() -> None:
    """Test to find character encoding which is others."""
    _not_same_encoding(
        "shift-jis", set_encoding(_get_input(), encoding="euc-jp")
    )
