#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to confirm that selected path include a mount point of Linux."""

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import is_relative
from pyspartaproj.script.path.modify.mount.shared.get_linux_head import (
    get_mount_point,
)


def has_linux_head(path: Path) -> bool:
    """Confirm that selected path include a mount point of Linux.

    Args:
        path (Path): Path you want to confirm.

    Returns:
        bool: True if the mount point is included.
    """
    return is_relative(path, root_path=get_mount_point())
