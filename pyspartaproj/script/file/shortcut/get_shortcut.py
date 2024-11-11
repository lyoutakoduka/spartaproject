#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_shortcut(target_path: Path, shortcut_root: Path) -> Path:
    return Path(shortcut_root, target_path.name).with_suffix(".lnk")
