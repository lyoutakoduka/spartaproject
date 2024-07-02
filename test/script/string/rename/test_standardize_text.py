#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to standardize string for key of dictionary."""

from pyspartaproj.script.string.rename.standardize_text import StandardizeText


def _compare_text(
    expected: str, source: str, standardize: StandardizeText
) -> None:
    assert expected == standardize.standardize(source)


def test_lower() -> None:
    """Test to convert upper case string to lower case."""
    _compare_text("test", "TEST", StandardizeText(lower=True))


def test_under() -> None:
    """Test to convert some characters to under bar."""
    for identifier in [" ", ".", "-"]:
        _compare_text(
            "test_name",
            identifier.join(["test", "name"]),
            StandardizeText(under=True),
        )


def test_strip() -> None:
    """Test to remove under bar of the both ends."""
    _compare_text("test", "__test__", StandardizeText(strip=True))
