#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def create_shortcut(shortcut_target: Path, shortcut_path: Path) -> bool:
    if not shortcut_target.exists():
        raise FileNotFoundError(shortcut_target)

    if shortcut_path.exists():
        return False

    return True
