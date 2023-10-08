#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Call designated function of designated module."""

from pathlib import Path

from pyspartaproj.interface.pytest import raises
from pyspartaproj.script.execute.call_module import call_function
from pyspartaproj.script.feature_flags import in_development

_source_path: Path = Path(__file__)


def test_unknown_module() -> None:
    """Unknown function calling of designated module."""
    error_path = Path(_source_path).with_name("unknown.py")

    if in_development():
        with raises(FileNotFoundError):
            call_function(_source_path, error_path)


def test_unknown_function() -> None:
    """Main function calling of unknown module."""
    other_path = Path(_source_path).with_name("debug_launcher.py")

    if in_development():
        with raises(ModuleNotFoundError):
            call_function(other_path, _source_path, function="unknown")


def main() -> bool:
    """Test all public functions.

    Returns:
        bool: success if get to the end of function
    """
    test_unknown_module()
    test_unknown_function()
    return True
