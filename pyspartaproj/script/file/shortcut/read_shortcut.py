#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.execute.execute_powershell import (
    get_path_string,
    get_quoted_paths,
    get_script_executable,
)


def _get_script_path() -> Path:
    return Path(Path(__file__).parent, "execute", "read.ps1")


def _get_shortcut_command(shortcut_path: Path) -> str:
    return get_script_executable(
        [
            get_path_string(_get_script_path()),
            get_quoted_paths(shortcut_path),
        ]
    )


def read_shortcut(shortcut_path: Path) -> Path:
    if not shortcut_path.exists():
        raise FileNotFoundError()

    return shortcut_path
