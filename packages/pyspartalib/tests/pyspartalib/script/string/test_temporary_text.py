#!/usr/bin/env python

"""Test module to show simple numbers as string type."""

from pyspartalib.context.type_context import Type
from pyspartalib.script.string.temporary_text import temporary_text


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def test_count() -> None:
    """Test to show number as string type by using "count" argument."""
    _difference_error(temporary_text(3, 1), ["0", "1", "2"])


def test_digit() -> None:
    """Test to show number as string type by using "digit" argument."""
    _difference_error(temporary_text(1, 3), ["000"])
