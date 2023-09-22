#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_shortcut_path(shortcut_target: Path, target_root: Path) -> Path:
    return Path(target_root, shortcut_target.name + '.lnk')
