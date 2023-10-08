#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.shell.execute_powershell import (
    execute_powershell,
    get_path_string,
    get_quoted_paths,
    get_script_executable,
)


def _get_script_path() -> Path:
    return Path(Path(__file__).parent, "resource", "read.ps1")


def _get_shortcut_command(shortcut_path: Path) -> str:
    return get_script_executable(
        [
            get_path_string(_get_script_path()),
            get_quoted_paths(shortcut_path),
        ]
    )


def read_shortcut(shortcut_path: Path) -> Path | None:
    if not shortcut_path.exists():
        raise FileNotFoundError()

    command_text: str = _get_shortcut_command(shortcut_path)
    result: Strs = execute_powershell(command_text)

    if 1 == len(result):
        return Path(result[0])

    return None
