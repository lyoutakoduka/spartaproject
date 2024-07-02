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


def test_all() -> None:
    _compare_text(
        "name_domain_com",
        " name@domain.com ",
        StandardizeText(lower=True, under=True, strip=True),
    )
