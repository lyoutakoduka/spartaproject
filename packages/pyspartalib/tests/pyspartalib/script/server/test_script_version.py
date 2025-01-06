#!/usr/bin/env python

"""Test module to get version information of Python interpreter."""

from pathlib import Path
from platform import python_version
from sys import executable

from pyspartalib.context.type_context import Type
from pyspartalib.script.server.script_version import (
    get_interpreter_version,
    get_version_name,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def test_name() -> None:
    """Test function to compare version string like default directory name."""
    version: str = "0.0.0"
    _difference_error(get_version_name(version), "Python-" + version)


def test_version() -> None:
    """Test function to compare version information of specific interpreter."""
    _difference_error(
        get_interpreter_version(Path(executable)),
        python_version(),
    )
