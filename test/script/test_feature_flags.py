#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Test of feature flags module."""

from pathlib import Path

from pyspartaproj.script.feature_flags import in_development
from pyspartaproj.script.stack_frame import current_frame


def _get_current_file() -> Path:
    return current_frame()["file"]


def test_develop() -> None:
    """Test when development environment."""
    assert in_development(__file__)


def test_production() -> None:
    """Test when production environment."""
    assert not in_development()


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_develop()
    test_production()
    return True
