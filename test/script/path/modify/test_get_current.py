#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get current working directory."""

from pyspartaproj.script.path.modify.get_current import get_current


def test_current() -> None:
    """Test to cet current working directory."""
    assert get_current().exists()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_current()
    return True
