#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from spartaproject.script.execute.virtual_environment import \
    virtual_environment


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_simple() -> None:
    """Creating primitive mode virtual environment."""
    def individual_test(environment_root: Path) -> None:
        assert virtual_environment(environment_root)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_simple()
    return True
