#!/usr/bin/env python

"""Test module to read Windows shortcut information from PowerShell."""

from pathlib import Path

import pytest
from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathPair
from pyspartalib.script.directory.working.working_date_time import (
    create_working_space,
)
from pyspartalib.script.file.shortcut.create_shortcut import create_shortcut
from pyspartalib.script.file.shortcut.get_shortcut import get_shortcut
from pyspartalib.script.file.shortcut.read_shortcut import read_shortcut
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.project.project_context import ProjectContext


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _get_config_file() -> Path:
    return get_resource(local_path=Path("forward.json"))


def _get_project_context() -> ProjectContext:
    return ProjectContext(forward=_get_config_file())


def _get_shared_paths() -> PathPair:
    return _get_project_context().get_path_context("shortcut")


def _get_temporary_windows() -> Path:
    return _get_shared_paths()["temporary.path"]


def _create_working_space() -> Path:
    return create_working_space(_get_temporary_windows(), jst=True)


def _create_shortcut(shortcut_target: Path, shortcut_path: Path) -> bool:
    return create_shortcut(
        shortcut_target,
        shortcut_path,
        forward=_get_config_file(),
    )


def _read_shortcut(shortcut_path: Path) -> Path:
    return _none_error(
        read_shortcut(shortcut_path, forward=_get_config_file()),
    )


def _compare_target(expected: Path, shortcut_path: Path) -> None:
    _difference_error(_read_shortcut(shortcut_path), expected)


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
        shortcut_target,
        get_shortcut(shortcut_target, shortcut_target),
    )


def test_exist() -> None:
    """Test to exists shortcut file before read inside it."""
    with pytest.raises(FileNotFoundError):
        read_shortcut(Path("empty.lnk"))
