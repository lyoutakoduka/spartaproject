#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert string by using the split identifier."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.split_identifier import SplitIdentifier


def _compare_identifier(
    identifier: str, split_identifier: SplitIdentifier
) -> None:
    assert identifier == split_identifier.get_identifier()


def test_path() -> None:
    """Test to get default split identifier."""
    _compare_identifier("_", SplitIdentifier())


def test_specific() -> None:
    """Test to get selected split identifier."""
    identifier: str = "-"
    _compare_identifier(identifier, SplitIdentifier(identifier=identifier))


def test_strip() -> None:
    """Test to remove the split identifier of the both ends."""
    expected: str = "test"
    assert expected == SplitIdentifier().convert_strip("__" + expected + "__")


def test_identifier() -> None:
    """Test to convert some characters to the split identifier.

    Candidates are characters other than alphabets and numbers.
    """
    names: Strs = ["first", "second", "third"]

    for identifier in [" ", ".", "-", "~"]:
        assert "_".join(names) == SplitIdentifier().convert_under(
            identifier.join(names)
        )
