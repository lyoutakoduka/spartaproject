#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.script.string.encoding.set_encoding import set_encoding


def _compare_encoding(expected: bytes, result: bytes) -> None:
    assert expected == result


def test_utf() -> None:
    source_text: str = "\u3042"
    expected: bytes = b"\xe3\x81\x82"

    _compare_encoding(expected, set_encoding(source_text))
