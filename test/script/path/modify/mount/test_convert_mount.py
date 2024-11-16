#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert shared path between Linux and Windows."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.mount.convert_mount import convert_mount


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_target_path(drive_identifier: str) -> Path:
    return Path(_get_mount_root(), drive_identifier, _get_relative_root())


def _get_expected_path(drive_identifier: str) -> Path:
    return Path(drive_identifier + ":", _get_relative_root())


def test_mount() -> None:
    """Test to convert shared path between Linux and Windows."""
    relative_root: Path = _get_relative_root()
    expected: Path = _get_expected_path("C")

    for path in [_get_target_path("c"), expected]:
        assert expected == convert_mount(path)
