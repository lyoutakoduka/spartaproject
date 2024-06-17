#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to show simple numbers as string type."""

from pyspartaproj.script.string.temporary_text import temporary_text


def test_count() -> None:
    """Test to show number as string type by using "count" argument."""
    assert ["0", "1", "2"] == temporary_text(3, 1)


def test_digit() -> None:
    """Test to show number as string type by using "digit" argument."""
    assert ["000"] == temporary_text(1, 3)
