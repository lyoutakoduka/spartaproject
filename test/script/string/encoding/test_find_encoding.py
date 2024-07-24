#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to find character encoding from string automatically."""

from pyspartaproj.script.string.encoding.find_encoding import find_encoding
from pyspartaproj.script.string.encoding.set_encoding import set_encoding


def _same_encoding(expected: str, result: bytes) -> None:
    assert expected == find_encoding(result)


def _not_same_encoding(expected: str, result: bytes) -> None:
    assert expected != find_encoding(result)


def _compare_encoding(encoding: str) -> None:
    _same_encoding(encoding, set_encoding(chr(12354), encoding=encoding))


def test_utf() -> None:
    """Test to find character encoding which is UTF-8."""
    _compare_encoding("utf-8")


def test_sjis() -> None:
    """Test to find character encoding which is Shift JIS."""
    _compare_encoding("shift-jis")


def test_other() -> None:
    """Test to find character encoding which is others."""
    _not_same_encoding(
        "shift-jis", set_encoding(chr(12354), encoding="euc-jp")
    )
