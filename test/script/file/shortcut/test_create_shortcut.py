#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create Windows shortcut from PowerShell."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.interface.pytest import raises
from pyspartaproj.script.file.shortcut.create_shortcut import create_shortcut
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _get_shortcut_path(shortcut_target: Path, shortcut_root: Path) -> Path:
    return Path(shortcut_root, shortcut_target.name + ".lnk")


def _common_test(shortcut_target: Path, shortcut_root: Path) -> None:
    shortcut_path: Path = _get_shortcut_path(shortcut_target, shortcut_root)
    create_shortcut(shortcut_target, shortcut_path)

    assert shortcut_path.exists()
    assert shortcut_target.name == shortcut_path.stem


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to create file type shortcut of Windows from PowerShell."""

    def individual_test(temporary_root: Path) -> None:
        source_path: Path = create_temporary_file(temporary_root)
        _common_test(source_path, temporary_root)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to create directory type shortcut of Windows from PowerShell."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(temporary_root, temporary_root)

    _inside_temporary_directory(individual_test)


def test_exist() -> None:
    """Test to exists shortcut file before create it."""

    def individual_test(temporary_root: Path) -> None:
        with raises(FileNotFoundError):
            _common_test(Path("empty"), temporary_root)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_directory()
    test_exist()
    return True
