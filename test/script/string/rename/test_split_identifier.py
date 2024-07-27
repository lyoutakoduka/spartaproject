#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert string by using the split identifier."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.split_identifier import SplitIdentifier


def _compare_identifier(
    identifier: str, split_identifier: SplitIdentifier
) -> None:
    assert identifier == split_identifier.get_identifier()


def _get_identifier() -> str:
    return "_"


def test_path() -> None:
    """Test to get default split identifier."""
    _compare_identifier(_get_identifier(), SplitIdentifier())


def test_specific() -> None:
    """Test to get selected split identifier."""
    identifier: str = "-"
    _compare_identifier(identifier, SplitIdentifier(identifier=identifier))


def test_strip() -> None:
    """Test to remove the split identifier of the both ends."""
    expected: str = "test"
    identifier: str = _get_identifier() * 2

    assert expected == SplitIdentifier().convert_strip(
        identifier + expected + identifier
    )


def test_identifier() -> None:
    """Test to convert some characters to the split identifier.

    Candidates are characters other than alphabets and numbers.
    """
    names: Strs = ["first", "second", "third"]
    expected: str = _get_identifier().join(names)
    split_identifier = SplitIdentifier()

    for identifier in [" ", ".", "-", "~"]:
        assert expected == split_identifier.convert_under(
            identifier.join(names)
        )
