#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get path of a shortcut file on Windows environment."""

from pathlib import Path


def get_shortcut(target_path: Path, shortcut_root: Path) -> Path:
    """Get path of a shortcut file on Windows environment.

    Module support both file and directory.

    1. File:
        Name of the shortcut file is "target.extension.lnk"
            if the name of file is "target.extension".

    2. Directory:
        Name of the shortcut file is "target.lnk"
            if the name of directory is "target".

    Args:
        target_path (Path): Path you want to create the shortcut file.

        shortcut_root (Path):
            Path of directory that the shortcut file is created.

    Returns:
        Path: Path of the shortcut file that is created.
    """
    path: Path = Path(shortcut_root, target_path.name)
    return path.with_suffix(target_path.suffix + ".lnk")
