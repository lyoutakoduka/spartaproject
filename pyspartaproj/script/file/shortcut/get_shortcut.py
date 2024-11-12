#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get path of a shortcut file on Windows environment."""

from pathlib import Path


def get_shortcut(target_path: Path, shortcut_root: Path) -> Path:
    """Get path of a shortcut file on Windows environment.

    Args:
        target_path (Path): Path you want to create the shortcut file.

        shortcut_root (Path):
            Path of directory that the shortcut file is created.

    Returns:
        Path: Path of the shortcut file that is created.
    """
    return Path(shortcut_root, target_path.name).with_suffix(".lnk")
