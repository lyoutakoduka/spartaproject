#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert shared path between Linux and Windows."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.mount.convert_mount import convert_mount


def test_mount() -> None:
    """Test to convert shared path between Linux and Windows."""
    path_elements: Strs = ["A", "B", "C"]
    expected: Path = Path("C:/", *path_elements)

    for path in [Path("/", "mnt", "c", *path_elements), expected]:
        assert expected == convert_mount(path)
