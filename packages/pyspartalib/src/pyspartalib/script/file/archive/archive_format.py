#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get information of archive format."""

from pathlib import Path


def get_format() -> str:
    """Get information of archive format.

    Returns:
        str: Archive format.
    """
    return "zip"


def rename_format(path: Path) -> Path:
    """Add archive format to path you select.

    Args:
        path (Path): Path you want to add archive format.

    Returns:
        Path: Path which added archive format.
    """
    return path.with_suffix("." + get_format())
