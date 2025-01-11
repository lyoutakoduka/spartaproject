#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to module to convert path from format Windows to format Linux."""

from pathlib import Path

from pyspartalib.script.path.modify.mount.build_linux_path import (
    get_linux_path,
)
from pyspartalib.script.path.modify.mount.build_windows_path import (
    get_windows_path,
)
from pyspartalib.script.path.modify.mount.convert_to_linux import (
    convert_to_linux,
)


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_windows_path() -> Path:
    return get_windows_path(_get_drive_letter(), _get_relative_root())


def _get_linux_path() -> Path:
    return get_linux_path(_get_drive_letter(), _get_relative_root())


def test_mount() -> None:
    """Test to convert path from format Windows to format Linux."""
    expected: Path = _get_linux_path()

    for path in [_get_windows_path(), expected]:
        assert expected == convert_to_linux(path)
