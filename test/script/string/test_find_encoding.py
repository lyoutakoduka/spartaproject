#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.find_encoding import find_encoding


def test_utf() -> None:
    target: str = chr(12354)
    byte: bytes = target.encode()
    encoding: str = find_encoding(byte)
    assert "utf-8" == encoding


def main() -> bool:
    test_utf()
    return True
