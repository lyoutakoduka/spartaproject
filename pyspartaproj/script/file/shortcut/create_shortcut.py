#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.execute.execute_powershell import (
    execute_powershell,
    get_path_string,
    get_quoted_paths,
    get_script_executable,
)
from pyspartaproj.script.path.safe.safe_trash import SafeTrash


def _get_path_string(path: Path) -> str:
    return str(path)  # Not as_posix()


def _get_script_path() -> Path:
    return Path(Path(__file__).parent, "execute", "create.ps1")


def _get_quoted_paths(shortcut_target: Path, shortcut_path: Path) -> Strs:
    return [
        _get_path_string(path).join(["'"] * 2)
        for path in [
            shortcut_target,
            shortcut_path,
        ]
    ]


def _get_powershell_command(commands_execute: Strs) -> str:
    return " ".join(commands_execute).join(['"'] * 2)


def _get_shortcut_command(shortcut_target: Path, shortcut_path: Path) -> str:
    shortcut_target_text: str = get_path_string(_get_script_path())
    commands_quoted: Strs = [
        get_quoted_paths(path) for path in [shortcut_target, shortcut_path]
    ]
    commands_execute: Strs = [shortcut_target_text] + commands_quoted
    return get_script_executable(commands_execute)


def create_shortcut(shortcut_target: Path, shortcut_path: Path) -> bool:
    if not shortcut_target.exists():
        raise FileNotFoundError()

    if shortcut_path.exists():
        safe_trash = SafeTrash()
        safe_trash.trash(shortcut_path)

    execute_powershell(_get_shortcut_command(shortcut_target, shortcut_path))

    return True
