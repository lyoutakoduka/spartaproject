#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to read Windows shortcut information from PowerShell."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.file.shortcut.create_shortcut import create_shortcut
from pyspartaproj.script.file.shortcut.read_shortcut import read_shortcut
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _get_config_file() -> Path:
    return get_resource(local_path=Path("execute_powershell", "forward.json"))


def _read_shortcut(shortcut_path: Path) -> Path:
    if shortcut_target := read_shortcut(
        shortcut_path, forward=_get_config_file()
    ):
        return shortcut_target
    else:
        fail()


def _get_shortcut_path(shortcut_target: Path, shortcut_root: Path) -> Path:
    return Path(shortcut_root, shortcut_target.name + ".lnk")


def _common_test(shortcut_target: Path, shortcut_root: Path) -> None:
    shortcut_path: Path = _get_shortcut_path(shortcut_target, shortcut_root)
    create_shortcut(shortcut_target, shortcut_path, forward=_get_config_file())

    assert shortcut_target == _read_shortcut(shortcut_path)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to read file type shortcut of Windows from PowerShell."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(create_temporary_file(temporary_root), temporary_root)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to read directory type shortcut of Windows from PowerShell."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(temporary_root, temporary_root)

    _inside_temporary_directory(individual_test)


def test_exist() -> None:
    """Test to exists shortcut file before read inside it."""
    with raises(FileNotFoundError):
        read_shortcut(Path("empty.lnk"))
