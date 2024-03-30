#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to standardize string for key of dictionary."""

from pyspartaproj.script.string.standardize_text import standardize_text


def test_lower() -> None:
    """Test to convert upper case string to lower case."""
    assert "test" == standardize_text("TEST")


def test_under() -> None:
    """Test to convert some characters to under bar."""
    for identifier in [" ", ".", "-"]:
        assert "test_name" == standardize_text(
            identifier.join(["test", "name"])
        )


def test_strip() -> None:
    """Test to remove under bar of the both ends."""
    assert "test" == standardize_text("__test__")


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_lower()
    test_under()
    test_strip()
    return True
