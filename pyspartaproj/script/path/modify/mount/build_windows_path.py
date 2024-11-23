#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get path about Windows file system."""

from pathlib import Path


def get_windows_head(identifier: str) -> Path:
    """Get root path of drive about Windows file system.

    Args:
        identifier (str): Drive letter you want to specify.

    Returns:
        Path: Path including the drive letter.
    """
    return Path(identifier.capitalize() + ":")


def get_windows_path(identifier: str, relative_root: Path) -> Path:
    """Generate path about Windows file system from elements.

    Args:
        identifier (str): Drive letter you want to specify.

        relative_root (Path):
            Relative path used for combining with the drive letter.

    Returns:
        Path: Generated path that is about Windows file system.
    """
    return Path(get_windows_head(identifier), relative_root)
