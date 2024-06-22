#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.script.string.translate_single import translate_single


def _common_test(expected: str, text: str) -> None:
    assert expected == translate_single(text)


def test_error() -> None:
    text: str = "\u3042"
    expected: str = text

    _common_test(expected, text)
