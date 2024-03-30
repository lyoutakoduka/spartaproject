#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.standardize_text import standardize_text


def test_lower() -> None:
    assert "test" == standardize_text("TEST")


def test_under() -> None:
    for identifier in [" ", "."]:
        assert "test_name" == standardize_text(
            identifier.join(["test", "name"])
        )


def main() -> bool:
    test_lower()
    test_under()
    return True
