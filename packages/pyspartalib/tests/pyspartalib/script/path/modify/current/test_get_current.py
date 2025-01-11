#!/usr/bin/env python

"""Test module to get current working directory."""

from pathlib import Path

from pyspartalib.script.path.modify.current.get_current import get_current


def _no_exists_error(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError


def test_current() -> None:
    """Test to cet current working directory."""
    _no_exists_error(get_current())
