#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.script.string.convert_type import convert_integer


def test_number() -> None:
    assert 1 == convert_integer("0001")


def main() -> bool:
    test_number()
    return True
