#! /usr/bin/env python

"""Test of feature flags module."""

from pathlib import Path

from pyspartalib.script.feature_flags import in_development
from pyspartalib.script.stack_frame import current_frame


def _get_current_file() -> Path:
    return current_frame()["file"]


def test_develop() -> None:
    """Test when development environment."""
    if not in_development(str(_get_current_file())):
        raise ValueError


def test_production() -> None:
    """Test when production environment."""
    if in_development():
        raise ValueError
