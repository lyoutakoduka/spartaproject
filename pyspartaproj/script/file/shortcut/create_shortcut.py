#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.shell.execute_powershell import (
    convert_mount_path,
    execute_powershell,
    get_quoted_paths,
    get_script_executable,
    get_script_string,
)


def _get_script_path() -> Path:
    return Path(Path(__file__).parent, "resource", "create.ps1")


def _get_shortcut_command(shortcut_target: Path, shortcut_path: Path) -> str:
    commands_quoted: Strs = [
        get_quoted_paths(convert_mount_path(path))
        for path in [shortcut_target, shortcut_path]
    ]

    return get_script_executable(
        [get_script_string(_get_script_path())] + commands_quoted
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


def create_shortcut(shortcut_target: Path, shortcut_path: Path) -> bool:
    _check_shortcut_exists(shortcut_target)

    if shortcut_path.exists():
        safe_trash = SafeTrash()
        safe_trash.trash(shortcut_path)

    _execute_script(shortcut_target, shortcut_path)
    return True
