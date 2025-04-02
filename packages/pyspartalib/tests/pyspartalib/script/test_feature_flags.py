#! /usr/bin/env python

"""Test of feature flags module."""

from pathlib import Path

from pyspartalib.script.feature_flags import in_development
from pyspartalib.script.frame.current_frame import CurrentFrame


def _success_error(status: bool) -> None:
    if status:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_current_file() -> Path:
    return CurrentFrame().get_frame()["file"]


def test_develop() -> None:
    """Test when development environment."""
    _fail_error(in_development(str(_get_current_file())))


def test_production() -> None:
    """Test when production environment."""
    _success_error(in_development())
