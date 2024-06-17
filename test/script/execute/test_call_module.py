#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Call designated function of designated module."""

from pathlib import Path

from pyspartaproj.interface.pytest import raises
from pyspartaproj.script.execute.call_module import call_function
from pyspartaproj.script.feature_flags import in_development
from pyspartaproj.script.stack_frame import current_frame


def _get_current_file() -> Path:
    return current_frame()["file"]


def test_unknown_module() -> None:
    """Unknown function calling of designated module."""
    current_file: Path = _get_current_file()
    error_path = Path(current_file).with_name("unknown.py")

    if in_development():
        with raises(FileNotFoundError):
            call_function(current_file, error_path)


def test_unknown_function() -> None:
    """Main function calling of unknown module."""
    current_file: Path = _get_current_file()
    other_path = Path(current_file).with_name("debug_launcher.py")

    if in_development():
        with raises(ModuleNotFoundError):
            call_function(other_path, current_file, function="unknown")
