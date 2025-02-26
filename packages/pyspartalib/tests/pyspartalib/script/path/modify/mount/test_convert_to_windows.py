#!/usr/bin/env python

"""Test module to convert path from format Linux to format Windows."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.path.modify.mount.build_linux_path import (
    get_linux_path,
)
from pyspartalib.script.path.modify.mount.build_windows_path import (
    get_windows_path,
)
from pyspartalib.script.path.modify.mount.convert_to_windows import (
    convert_to_windows,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_windows_path() -> Path:
    return get_windows_path(_get_drive_letter(), _get_relative_root())


def _get_linux_path() -> Path:
    return get_linux_path(_get_drive_letter(), _get_relative_root())


def test_mount() -> None:
    """Test to convert path from format Linux to format Windows."""
    expected: Path = _get_windows_path()

    for path in [_get_linux_path(), expected]:
        _difference_error(convert_to_windows(path), expected)
