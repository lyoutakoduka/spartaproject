#!/usr/bin/env python

"""Test module to convert text to specific type."""

from pyspartalib.script.string.convert_type import convert_integer


def test_number() -> None:
    """Test to convert text to type "integer"."""
    assert convert_integer("0001") == 1


def test_error() -> None:
    """Test to convert text, but it's not number."""
    assert convert_integer("error") is None
