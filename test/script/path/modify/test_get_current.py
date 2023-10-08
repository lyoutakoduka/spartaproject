#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.path.modify.get_current import get_current


def test_current() -> None:
    assert get_current().exists()


def main() -> bool:
    test_current()
    return True
