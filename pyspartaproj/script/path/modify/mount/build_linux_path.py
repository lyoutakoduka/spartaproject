#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_mount_point() -> Path:
    """Get the path of a mount point of Linux.

    Returns:
        Path: Path of the mount point.
    """
    return Path("/", "mnt")


def get_linux_head(identifier: str) -> Path:
    return Path(get_mount_point(), identifier.lower())


def build_linux_path(identifier: str, relative_root: Path) -> Path:
    return Path(get_linux_head(identifier), relative_root)
