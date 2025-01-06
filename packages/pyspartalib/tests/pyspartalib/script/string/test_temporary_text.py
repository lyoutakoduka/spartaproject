#!/usr/bin/env python

"""Test module to show simple numbers as string type."""

from pyspartalib.script.string.temporary_text import temporary_text


def test_count() -> None:
    """Test to show number as string type by using "count" argument."""
    assert temporary_text(3, 1) == ["0", "1", "2"]


def test_digit() -> None:
    """Test to show number as string type by using "digit" argument."""
    assert temporary_text(1, 3) == ["000"]
