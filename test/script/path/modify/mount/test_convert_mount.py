#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert shared path between Linux and Windows."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.mount.convert_mount import convert_mount


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _get_target_path(drive_identifier: str, relative_root: Path) -> Path:
    return Path(_get_mount_root(), drive_identifier, relative_root)


def test_mount() -> None:
    """Test to convert shared path between Linux and Windows."""
    path_elements: Strs = ["A", "B", "C"]
    expected: Path = Path("C:/", *path_elements)
    relative_root: Path = Path(*path_elements)

    for path in [_get_target_path("c", relative_root), expected]:
        assert expected == convert_mount(path)
