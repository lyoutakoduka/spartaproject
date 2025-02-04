#!/usr/bin/env python

"""Test module to get current working directory."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.path.modify.current.get_current import get_current


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _no_exists_error(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError


def test_current() -> None:
    """Test to cet current working directory."""
    _no_exists_error(get_current())
