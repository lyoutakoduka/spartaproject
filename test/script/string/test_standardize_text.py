#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.standardize_text import standardize_text


def test_lower() -> None:
    assert "test" == standardize_text("TEST")


def main() -> bool:
    test_lower()
    return True
