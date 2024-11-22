#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to confirm that selected path include a mount point of Linux."""

from pathlib import Path

from pyspartaproj.context.default.bool_context import Bools
from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.path.modify.mount.build_linux_path import (
    get_linux_path,
)
from pyspartaproj.script.path.modify.mount.build_windows_path import (
    get_windows_path,
)
from pyspartaproj.script.path.modify.mount.shared.has_linux_head import (
    has_linux_head,
)


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_windows_path() -> Path:
    return get_windows_path(_get_drive_letter(), _get_relative_root())


def _get_linux_path() -> Path:
    return get_linux_path(_get_drive_letter(), _get_relative_root())


def _get_expected() -> Bools:
    return [True, False]


def _get_paths() -> Paths:
    return [_get_linux_path(), _get_windows_path()]


def test_mount() -> None:
    """Test to confirm that selected path include a mount point of Linux."""
    for expected, path in zip(_get_expected(), _get_paths()):
        assert expected == has_linux_head(path)
