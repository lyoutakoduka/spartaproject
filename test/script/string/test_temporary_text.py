#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.temporary_text import temporary_text


def test_count() -> None:
    assert ["0", "1", "2"] == temporary_text(3, 1)


def test_order() -> None:
    assert ["000"] == temporary_text(1, 3)


def main() -> bool:
    test_count()
    test_order()
    return True
