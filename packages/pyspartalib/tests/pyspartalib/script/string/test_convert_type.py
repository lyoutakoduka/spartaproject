#!/usr/bin/env python

"""Test module to convert text to specific type."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.string.convert_type import convert_integer


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _not_none_error(result: object) -> None:
    if result is not None:
        raise ValueError


def test_number() -> None:
    """Test to convert text to type "integer"."""
    _difference_error(convert_integer("0001"), 1)


def test_error() -> None:
    """Test to convert text, but it's not number."""
    _not_none_error(convert_integer("error"))
