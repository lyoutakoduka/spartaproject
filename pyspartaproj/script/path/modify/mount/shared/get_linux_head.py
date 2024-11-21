#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get the path of a mount point of Linux."""

from pathlib import Path


def get_linux_head() -> Path:
    """Get the path of a mount point of Linux.

    Returns:
        Path: Path of the mount point.
    """
    return Path("/", "mnt")
