#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get relative path seen from a mount point of Linux."""

from pathlib import Path

from pyspartalib.script.path.modify.mount.build_linux_path import (
    get_linux_path,
)
from pyspartalib.script.path.modify.mount.shared.get_linux_relative import (
    get_linux_relative,
)


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_expected_path() -> Path:
    return Path(_get_drive_letter(), _get_relative_root())


def _get_linux_path() -> Path:
    return get_linux_path(_get_drive_letter(), _get_relative_root())


def test_mount() -> None:
    """Test to get relative path seen from a mount point of Linux."""
    assert _get_expected_path() == get_linux_relative(_get_linux_path())
