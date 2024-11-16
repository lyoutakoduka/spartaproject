#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert shared path from for Linux to for Windows."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.mount.build_windows_path import (
    build_windows_path,
)
from pyspartaproj.script.path.modify.mount.shared.get_linux_relative import (
    get_linux_relative,
)
from pyspartaproj.script.path.modify.mount.shared.has_linux_head import (
    has_linux_head,
)


def _get_relative_strings(path: Path) -> Strs:
    return list(get_linux_relative(path).parts)


def _get_drive_letter(path: Path) -> str:
    return _get_relative_strings(path)[0]


def _get_relative_root(path: Path) -> Path:
    return Path(*_get_relative_strings(path)[1:])


def convert_to_windows(path: Path) -> Path:
    """Convert shared path from for Linux to for Windows.

    e.g., if you select argument (path) like "/mnt/c/Users/user",
        "C:/Users/user" is returned.

    Args:
        path (Path): Linux path which is starts from mount string.

    Returns:
        Path: Converted Windows path which is starts from drive letter.
    """
    if not has_linux_head(path):
        return path

    return build_windows_path(
        _get_drive_letter(path), _get_relative_root(path)
    )
