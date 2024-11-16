#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert shared path between Linux and Windows."""

from pathlib import Path


def convert_mount_path(path: Path) -> Path:
    """Convert shared path between Linux and Windows.

    e.g., if you select argument (path) like "/mnt/c/Users/user",
        "C:/Users/user" is returned.

    Args:
        path (Path): Linux path which is starts from mount string.

    Returns:
        Path: Converted Windows path which is starts from drive letter.
    """
    path_text: str = path.as_posix()
    mount: str = "/mnt/"

    if not path_text.startswith(mount):
        return path

    index: int = len(mount)
    index_right: int = index + 1

    return Path(path_text[index].capitalize() + ":" + path_text[index_right:])
