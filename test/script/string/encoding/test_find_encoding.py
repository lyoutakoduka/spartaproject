#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to find character encoding from string automatically."""

from pyspartaproj.script.string.encoding.find_encoding import find_encoding


def _common_test(encoding: str) -> None:
    assert encoding == find_encoding(chr(12354).encode(encoding))


def test_utf() -> None:
    """Test to find character encoding which is UTF-8."""
    _common_test("utf-8")


def test_sjis() -> None:
    """Test to find character encoding which is Shift JIS."""
    _common_test("shift-jis")


def test_other() -> None:
    """Test to find character encoding which is others."""
    assert "shift-jis" != find_encoding(chr(12354).encode("euc-jp"))
