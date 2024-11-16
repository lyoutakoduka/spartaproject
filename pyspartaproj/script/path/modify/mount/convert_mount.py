#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert shared path between Linux and Windows."""

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import is_relative


def convert_mount(path: Path) -> Path:
    """Convert shared path between Linux and Windows.

    e.g., if you select argument (path) like "/mnt/c/Users/user",
        "C:/Users/user" is returned.

    Args:
        path (Path): Linux path which is starts from mount string.

    Returns:
        Path: Converted Windows path which is starts from drive letter.
    """
    mount_root: Path = Path("/", "mnt")

    if not is_relative(path, root_path=mount_root):
        return path

    path_text: str = path.as_posix()
    mount: str = "/mnt/"
    index: int = len(mount)
    index_right: int = index + 1

    return Path(path_text[index].capitalize() + ":" + path_text[index_right:])
