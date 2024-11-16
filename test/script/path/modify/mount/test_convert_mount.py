#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert shared path between Linux and Windows."""

from pathlib import Path

from pyspartaproj.script.path.modify.mount.convert_mount import convert_mount


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _convert_linux(identifier: str) -> Path:
    return Path(_get_mount_root(), identifier.lower())


def _convert_windows(identifier: str) -> Path:
    return Path(identifier.capitalize() + ":")


def _get_linux_path(identifier: str, relative_root: Path) -> Path:
    return Path(_convert_linux(identifier), relative_root)


def _get_windows_path(identifier: str, relative_root: Path) -> Path:
    return Path(_convert_windows(identifier), relative_root)


def _get_target_path() -> Path:
    return _get_linux_path(_get_drive_letter(), _get_relative_root())


def _get_expected_path() -> Path:
    return _get_windows_path(_get_drive_letter(), _get_relative_root())


def test_mount() -> None:
    """Test to convert shared path between Linux and Windows."""
    expected: Path = _get_expected_path()

    for path in [_get_target_path(), expected]:
        assert expected == convert_mount(path)
