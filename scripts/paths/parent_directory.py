#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from scripts.paths.create_directory import path_mkdir


def create_parent_dir(child_path: Path) -> Path:
    path: Path = child_path.parent
    if path.exists():
        return path
    return path_mkdir(path)
