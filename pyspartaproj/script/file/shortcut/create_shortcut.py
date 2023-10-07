#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _get_path_string(path: Path) -> str:
    return str(path)  # Not as_posix()


def _get_script_path() -> Path:
    current: Path = Path(__file__)
    return Path(
        current.parent,
        "execute",
        current.with_suffix(".ps1").name,
    )


def create_shortcut(shortcut_target: Path, shortcut_path: Path) -> bool:
    if not shortcut_target.exists():
        raise FileNotFoundError(shortcut_target)

    if shortcut_path.exists():
        return False

    return True
