#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.file.archive.archive_format import get_format


def test_format() -> None:
    assert "zip" == get_format()


def main() -> bool:
    test_format()
    return True
