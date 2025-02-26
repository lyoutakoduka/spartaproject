#!/usr/bin/env python

"""Module to create all parent directories of the path you select."""

from pathlib import Path

from pyspartalib.script.directory.create_directory import create_directory


def create_parent(child_path: Path) -> Path:
    """Create all parent directories of the path you select if not exists.

    Args:
        child_path (Path): Child path for creating parent directories.

    Returns:
        Path: Path of created parent directories.

    """
    path: Path = child_path.parent

    if path.exists():
        return path

    return create_directory(path)
