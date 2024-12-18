#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to read Windows shortcut information from PowerShell."""

from pathlib import Path

from pyspartalib.context.extension.path_context import PathPair
from pyspartalib.script.directory.date_time_space import create_working_space
from pyspartalib.script.file.shortcut.create_shortcut import create_shortcut
from pyspartalib.script.file.shortcut.get_shortcut import get_shortcut
from pyspartalib.script.file.shortcut.read_shortcut import read_shortcut
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.project.project_context import ProjectContext
from tests.pyspartalib.interface.pytest import fail, raises


def _get_config_file() -> Path:
    return get_resource(local_path=Path("forward.json"))


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


def _compare_target(expected: Path, shortcut_path: Path) -> None:
    assert expected == _read_shortcut(shortcut_path)


def _common_test(shortcut_target: Path, shortcut_path: Path) -> None:
    _create_shortcut(shortcut_target, shortcut_path)
    _compare_target(shortcut_target, shortcut_path)


def test_file() -> None:
    """Test to read file type shortcut of Windows from PowerShell."""
    working_space: Path = _create_working_space()
    shortcut_target: Path = create_temporary_file(working_space)

    _common_test(shortcut_target, get_shortcut(shortcut_target, working_space))


def test_directory() -> None:
    """Test to read directory type shortcut of Windows from PowerShell."""
    shortcut_target: Path = _create_working_space()

    _common_test(
        shortcut_target, get_shortcut(shortcut_target, shortcut_target)
    )


def test_exist() -> None:
    """Test to exists shortcut file before read inside it."""
    with raises(FileNotFoundError):
        read_shortcut(Path("empty.lnk"))
