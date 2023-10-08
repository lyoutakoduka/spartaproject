#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Test of feature flags module."""

from pyspartaproj.script.feature_flags import in_development


def test_develop() -> None:
    """Test when development environment."""
    assert in_development(__file__)


def test_production() -> None:
    """Test when production environment."""
    assert not in_development()


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: success if get to the end of function
    """
    test_develop()
    test_production()
    return True
