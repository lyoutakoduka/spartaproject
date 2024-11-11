#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.file.shortcut.get_shortcut import get_shortcut


def test_file() -> None:
    target_root: Path = Path("root", "create", "target")
    shortcut_root: Path = Path("root", "created")
    expected: Path = Path("root", "created", "target.lnk")

    assert expected == get_shortcut(target_root, shortcut_root)
