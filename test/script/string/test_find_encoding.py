#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.find_encoding import find_encoding


def _common_test(encoding: str) -> None:
    assert encoding == find_encoding(chr(12354).encode(encoding))


def test_utf() -> None:
    _common_test("utf-8")


def test_sjis() -> None:
    _common_test("shift-jis")


def main() -> bool:
    test_utf()
    test_sjis()
    return True
