#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.rename.split_identifier import SplitIdentifier


def _compare_identifier(
    identifier: str, split_identifier: SplitIdentifier
) -> None:
    assert identifier == split_identifier.get_identifier()


def test_path() -> None:
    _compare_identifier("_", SplitIdentifier())


def test_specific() -> None:
    identifier: str = "-"
    _compare_identifier(identifier, SplitIdentifier(identifier=identifier))


def test_strip() -> None:
    """Test to remove under bar of the both ends."""
    expected: str = "test"
    assert expected == SplitIdentifier().convert_strip("__" + expected + "__")