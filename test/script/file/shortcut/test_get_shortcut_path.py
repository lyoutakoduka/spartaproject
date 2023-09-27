#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.file.shortcut.get_shortcut_path import (
    get_shortcut_path,
)


def test_name() -> None:
    shortcut_target: Path = Path(__file__)
    target_root: Path = shortcut_target.parent
    expected: Path = shortcut_target.with_name(shortcut_target.name + ".lnk")

    assert expected == get_shortcut_path(shortcut_target, target_root)


def main() -> bool:
    test_name()
    return True
