#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert string by using the split identifier."""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.string.rename.split_identifier import SplitIdentifier


def _compare_text(expected: str, result: str) -> None:
    assert expected == result


def _compare_identifier(
    identifier: str, split_identifier: SplitIdentifier
) -> None:
    _compare_text(identifier, split_identifier.get_identifier())


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
        _compare_text(
            expected, split_identifier.convert_under(identifier.join(names))
        )


def test_replace() -> None:
    """Test to replace one or more consecutive split identifier."""
    base_identifier: str = _get_identifier()
    names: Strs = ["first", "second"]
    expected: str = base_identifier.join(names)
    split_identifier = SplitIdentifier()

    for i in range(3):
        identifier: str = base_identifier * (i + 1)
        _compare_text(
            expected,
            split_identifier.replace_identifier(identifier.join(names)),
        )


def test_switch() -> None:
    """Test to switch the split identifier to specific character."""
    base_identifier: str = " "
    expected: str = base_identifier.join(["first", "second"])
    split_identifier = SplitIdentifier()

    _compare_text(
        expected,
        split_identifier.switch_identifier(
            split_identifier.convert_under(expected), base_identifier
        ),
    )
