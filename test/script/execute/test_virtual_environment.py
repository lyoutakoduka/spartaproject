#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test to creating python virtual environment."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.script.execute.virtual_environment import \
    virtual_environment


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_simple() -> None:
    """Creating primitive mode virtual environment."""
    def individual_test(environment_root: Path) -> None:
        assert virtual_environment(environment_root)

    _inside_temporary_directory(individual_test)


def test_version() -> None:
    """Creating primitive mode virtual environment.

    by specific python version
    """
    versions: Ints = [3, 10, 11]

    def individual_test(environment_root: Path) -> None:
        assert virtual_environment(environment_root, versions=versions)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    # test_simple()
    test_version()
    return True
