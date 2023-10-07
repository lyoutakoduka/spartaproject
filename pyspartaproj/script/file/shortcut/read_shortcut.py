#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _get_script_path() -> Path:
    return Path(Path(__file__).parent, "execute", "read.ps1")


def read_shortcut(shortcut_path: Path) -> Path:
    if not shortcut_path.exists():
        raise FileNotFoundError()

    return shortcut_path
