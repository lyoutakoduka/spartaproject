#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create Windows shortcut from PowerShell."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.shell.execute_powershell import (
    convert_mount_path,
    execute_powershell,
    get_double_quoted_command,
    get_path_string,
    get_quoted_path,
    get_script_string,
)


def _get_quoted_command(shortcut_target: Path, shortcut_path: Path) -> Strs:
    return [
        get_quoted_path(get_path_string(convert_mount_path(path)))
        for path in [shortcut_target, shortcut_path]
    ]


def _get_resource_script() -> str:
    return get_script_string(get_resource(local_path=Path("create.ps1")))


def _get_shortcut_command(shortcut_target: Path, shortcut_path: Path) -> str:
    commands: Strs = [_get_resource_script()]
    return get_double_quoted_command(
        commands + _get_quoted_command(shortcut_target, shortcut_path)
    )


def _execute_script(shortcut_target: Path, shortcut_path: Path) -> None:
    list(
        execute_powershell(
            [_get_shortcut_command(shortcut_target, shortcut_path)]
        )
    )


def _check_shortcut_exists(shortcut_target: Path) -> None:
    if not shortcut_target.exists():
        raise FileNotFoundError()


def _cleanup_shortcut(shortcut_path: Path, remove_root: Path | None) -> None:
    if shortcut_path.exists():
        SafeTrash(remove_root=remove_root).trash(shortcut_path)


def create_shortcut(
    shortcut_target: Path, shortcut_path: Path, remove_root: Path | None = None
) -> bool:
    """Create Windows shortcut from PowerShell.

    Args:
        shortcut_target (Path): Path which is a link destination of shortcut.

        shortcut_path (Path): Path of shortcut you want to create.
            Extension of shortcut should be ".lnk".

    Returns:
        bool: True if creating shortcut is success.
    """
    _check_shortcut_exists(shortcut_target)
    _cleanup_shortcut(shortcut_path, remove_root)
    _execute_script(shortcut_target, shortcut_path)
    return True
