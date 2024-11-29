#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to read Windows shortcut information from PowerShell."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.directory.date_time_space import create_working_space
from pyspartaproj.script.file.shortcut.create_shortcut import create_shortcut
from pyspartaproj.script.file.shortcut.get_shortcut import get_shortcut
from pyspartaproj.script.file.shortcut.read_shortcut import read_shortcut
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.project.project_context import ProjectContext


def _get_config_file() -> Path:
    return get_resource(local_path=Path("execute_powershell", "forward.json"))


def _get_project_context() -> ProjectContext:
    return ProjectContext(forward=_get_config_file())


def _get_shared_paths() -> PathPair:
    return _get_project_context().get_path_context("share")


def _get_temporary_windows() -> Path:
    return _get_shared_paths()["temporary_windows.path"]


def _create_working_space() -> Path:
    return create_working_space(_get_temporary_windows(), jst=True)


def _create_shortcut(shortcut_target: Path, shortcut_path: Path) -> bool:
    return create_shortcut(
        shortcut_target, shortcut_path, forward=_get_config_file()
    )


def _read_shortcut(shortcut_path: Path) -> Path:
    if shortcut_target := read_shortcut(
        shortcut_path, forward=_get_config_file()
    ):
        return shortcut_target
    else:
        fail()


def _common_test(shortcut_target: Path, shortcut_root: Path) -> None:
    shortcut_path: Path = get_shortcut(shortcut_target, shortcut_root)
    create_shortcut(shortcut_target, shortcut_path, forward=_get_config_file())

    assert shortcut_target == _read_shortcut(shortcut_path)


def _compare_target(expected: Path, shortcut_path: Path) -> None:
    assert expected == _read_shortcut(shortcut_path)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to read file type shortcut of Windows from PowerShell."""
    working_space: Path = _create_working_space()
    shortcut_target: Path = create_temporary_file(working_space)
    shortcut_path: Path = get_shortcut(shortcut_target, working_space)

    _create_shortcut(shortcut_target, shortcut_path)
    _compare_target(shortcut_target, shortcut_path)


def test_directory() -> None:
    """Test to read directory type shortcut of Windows from PowerShell."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(temporary_root, temporary_root)

    _inside_temporary_directory(individual_test)


def test_exist() -> None:
    """Test to exists shortcut file before read inside it."""
    with raises(FileNotFoundError):
        read_shortcut(Path("empty.lnk"))
