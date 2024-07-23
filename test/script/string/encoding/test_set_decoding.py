#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to decode byte data by specific character encoding."""

from pyspartaproj.script.string.encoding.set_decoding import set_decoding


def _compare_decoding(result: str) -> None:
    assert "\u3042" == result


def test_utf() -> None:
    """Test to decode byte data by default character encoding."""
    source: bytes = b"\xe3\x81\x82"

    _compare_decoding(set_decoding(source))


def test_sjis() -> None:
    """Test to decode byte data by specific character encoding."""
    source: bytes = b"\x82\xa0"

    _compare_decoding(set_decoding(source, encoding="shift_jis"))
