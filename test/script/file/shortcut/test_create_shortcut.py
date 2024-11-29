#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create Windows shortcut from PowerShell."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.directory.date_time_space import create_working_space
from pyspartaproj.script.file.shortcut.create_shortcut import create_shortcut
from pyspartaproj.script.file.shortcut.get_shortcut import get_shortcut
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.status.check_exists import check_exists_array
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


def _create_shortcut_remove(
    shortcut_target: Path, shortcut_path: Path, remove_root: Path
) -> bool:
    return create_shortcut(
        shortcut_target,
        shortcut_path,
        remove_root=remove_root,
        forward=_get_config_file(),
    )


def _filter_created(is_success: bool) -> None:
    if not is_success:
        fail()


def _success_created(shortcut_target: Path, shortcut_path: Path) -> None:
    _filter_created(_create_shortcut(shortcut_target, shortcut_path))


def _success_created_remove(
    shortcut_target: Path, shortcut_path: Path, remove_root: Path
) -> None:
    _filter_created(
        _create_shortcut_remove(shortcut_target, shortcut_path, remove_root)
    )


def _confirm_exists(shortcut_target: Path, shortcut_path: Path) -> None:
    assert check_exists_array([shortcut_target, shortcut_path])


def _compare_name(shortcut_target: Path, shortcut_path: Path) -> None:
    assert shortcut_target.name == shortcut_path.stem


def _common_test(shortcut_target: Path, shortcut_path: Path) -> None:
    _confirm_exists(shortcut_target, shortcut_path)
    _compare_name(shortcut_target, shortcut_path)


def _get_shortcut_pair(temporary_root: Path) -> Strs:
    return [
        path.name
        for path in walk_iterator(
            temporary_root, directory=False, suffix="lnk"
        )
    ]


def _get_shortcut_names(roots: Paths) -> Strs:
    return [
        path.name
        for root in roots
        for path in walk_iterator(root, directory=False, suffix="lnk", depth=1)
    ]


def _compare_shortcut(temporary_root: Path) -> None:
    assert 1 == len(set(_get_shortcut_pair(temporary_root)))


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to create file type shortcut of Windows from PowerShell."""
    working_space: Path = _create_working_space()
    shortcut_target: Path = create_temporary_file(working_space)
    shortcut_path: Path = get_shortcut(shortcut_target, working_space)

    _success_created(shortcut_target, shortcut_path)
    _common_test(shortcut_target, shortcut_path)


def test_directory() -> None:
    """Test to create directory type shortcut of Windows from PowerShell."""
    shortcut_target: Path = _create_working_space()
    shortcut_path: Path = get_shortcut(shortcut_target, shortcut_target)

    _success_created(shortcut_target, shortcut_path)
    _common_test(shortcut_target, shortcut_path)


def test_exist() -> None:
    """Test to exists shortcut file before create it."""
    empty_path: Path = Path("empty")

    with raises(FileNotFoundError):
        create_shortcut(empty_path, empty_path)


def test_remove() -> None:
    """Test to remove shortcut file when overriding existing shortcut."""

    def individual_test(temporary_root: Path) -> None:
        shortcut_path: Path = get_shortcut(temporary_root, temporary_root)

        _filter_created(_create_shortcut(temporary_root, shortcut_path))
        _filter_created(
            _create_shortcut_remove(
                temporary_root, shortcut_path, Path(temporary_root, "result")
            )
        )

        _compare_shortcut(temporary_root)

    _inside_temporary_directory(individual_test)
