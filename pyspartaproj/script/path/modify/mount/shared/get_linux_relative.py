#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get relative path seen from a mount point of Linux."""

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import get_relative
from pyspartaproj.script.path.modify.mount.build_linux_path import (
    get_mount_point,
)


def get_linux_relative(path: Path) -> Path:
    """Get relative path seen from a mount point of Linux.

    Args:
        path (Path): Full path including the mount point.

    Returns:
        Path: Relative path which the mount point is removed.
    """
    return get_relative(path, root_path=get_mount_point())
