#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get path about Windows mounted on Linux."""

from pathlib import Path


def get_mount_point() -> Path:
    """Get the path of a mount point of Linux.

    Returns:
        Path: Path of the mount point.
    """
    return Path("/", "mnt")


def get_linux_head(identifier: str) -> Path:
    """Get path of a drive letter about Windows mounted on Linux.

    Args:
        identifier (str): Drive letter you want to specify.

    Returns:
        Path: Path including the drive letter.
    """
    return Path(get_mount_point(), identifier.lower())


def get_linux_path(identifier: str, relative_root: Path) -> Path:
    """Generate path about Windows mounted on Linux from elements.

    Args:
        identifier (str): Drive letter you want to specify.

        relative_root (Path):
            Relative path used for combining with the drive letter.

    Returns:
        Path: Generated path about Windows mounted on Linux.
    """
    return Path(get_linux_head(identifier), relative_root)
