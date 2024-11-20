#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get a path that drive of Windows will be mounted."""

from pathlib import Path


def get_linux_head() -> Path:
    """Get a path that drive of Windows will be mounted.

    Returns:
        Path: Path that drive will be mounted.
    """
    return Path("/", "mnt")
