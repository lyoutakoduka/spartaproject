#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert shared path between Linux and Windows."""

from pathlib import Path

from pyspartaproj.script.path.modify.mount.convert_mount import convert_mount


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_target_path(drive_identifier: str) -> Path:
    return Path(_get_mount_root(), drive_identifier, _get_relative_root())


def _get_expected_path(identifier: str) -> Path:
    return Path(identifier + ":", _get_relative_root())


def test_mount() -> None:
    """Test to convert shared path between Linux and Windows."""
    identifier: str = _get_drive_letter()
    expected: Path = _get_expected_path(identifier.capitalize())

    for path in [_get_target_path(identifier), expected]:
        assert expected == convert_mount(path)
