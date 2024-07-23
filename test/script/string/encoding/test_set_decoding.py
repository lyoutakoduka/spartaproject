#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.script.string.encoding.set_decoding import set_decoding


def _compare_decoding(result: str) -> None:
    assert "\u3042" == result


def test_utf() -> None:
    source: bytes = b"\xe3\x81\x82"

    _compare_decoding(set_decoding(source))
