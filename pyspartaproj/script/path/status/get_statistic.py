#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get statistics about file."""

from pathlib import Path


def get_file_size(path: Path) -> int:
    """Get size of file.

    Args:
        path (Path): Path of file you want to get size.

    Returns:
        int: File size.
    """
    return path.stat().st_size
