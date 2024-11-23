#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert path from format Windows to format Linux."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.mount.build_linux_path import (
    get_linux_path,
)
from pyspartaproj.script.path.modify.mount.shared.has_linux_head import (
    has_linux_head,
)


def _get_relative_strings(path: Path) -> Strs:
    return list(path.parts)


def _get_drive_letter(path: Path) -> str:
    return _get_relative_strings(path)[0][0]


def _get_relative_root(path: Path) -> Path:
    return Path(*_get_relative_strings(path)[1:])


def convert_to_linux(path: Path) -> Path:
    """Convert path from format Windows to format Linux.

    Args:
        path (Path): Windows format path you want to convert.

    Returns:
        Path: Converted Linux format path.
    """
    if has_linux_head(path):
        return path

    return get_linux_path(_get_drive_letter(path), _get_relative_root(path))
