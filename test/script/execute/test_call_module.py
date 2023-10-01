#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Call designated function of designated module."""

from pathlib import Path

from pytest import raises

from pyspartaproj.script.execute.call_module import call_function

_SOURCE_PATH: Path = Path(__file__)


def test_unknown_module() -> None:
    """Unknown function calling of designated module."""
    error_path = Path(_SOURCE_PATH).with_name("unknown.py")
    with raises(FileNotFoundError):
        call_function(_SOURCE_PATH, error_path)


def test_unknown_function() -> None:
    """Main function calling of unknown module."""
    other_path = Path(_SOURCE_PATH).with_name("debug.py")
    with raises(ModuleNotFoundError):
        call_function(other_path, _SOURCE_PATH, function="unknown")


def test_same() -> None:
    """Main function calling of designated module."""
    with raises(ValueError):
        call_function(_SOURCE_PATH, _SOURCE_PATH)


def main() -> bool:
    """Test all public functions.

    Returns:
        bool: success if get to the end of function
    """
    test_unknown_module()
    test_unknown_function()
    test_same()
    return True
