#! /usr/bin/env python

"""Test of feature flags module."""

from pathlib import Path

from pyspartalib.script.feature_flags import in_development
from pyspartalib.script.stack_frame import current_frame


def _success_error(status: bool) -> None:
    if status:
        raise ValueError


def _get_current_file() -> Path:
    return current_frame()["file"]


def test_develop() -> None:
    """Test when development environment."""
    if not in_development(str(_get_current_file())):
        raise ValueError


def test_production() -> None:
    """Test when production environment."""
    _success_error(in_development())
