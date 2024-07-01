#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to standardize string for key of dictionary."""

from pyspartaproj.script.string.rename.standardize_text import StandardizeText


def test_lower() -> None:
    """Test to convert upper case string to lower case."""
    assert "test" == StandardizeText(lower=True).standardize("TEST")


def test_under() -> None:
    """Test to convert some characters to under bar."""
    for identifier in [" ", ".", "-"]:
        assert "test_name" == StandardizeText(under=True).standardize(
            identifier.join(["test", "name"])
        )


def test_strip() -> None:
    """Test to remove under bar of the both ends."""
    assert "test" == standardize_text("__test__")
