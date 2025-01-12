#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get path of a shortcut file on Windows environment."""

from pathlib import Path

from pyspartalib.script.file.shortcut.get_shortcut import get_shortcut


def _get_target_root() -> Path:
    return Path("root", "create")


def _get_shortcut_root() -> Path:
    return Path("root", "created")


def _get_expected(target_name: str) -> Path:
    return Path(_get_shortcut_root(), target_name + ".lnk")


def _get_target(target_name: str) -> Path:
    return Path(_get_target_root(), target_name)


def _get_result(target_name: str) -> Path:
    return get_shortcut(_get_target(target_name), _get_shortcut_root())


def _compare_shortcut(target_name: str) -> None:
    assert _get_expected(target_name) == _get_result(target_name)


def test_file() -> None:
    """Test to get path of a shortcut file that target is file."""
    _compare_shortcut("target.extension")


def test_directory() -> None:
    """Test to get path of a shortcut file that target is directory."""
    _compare_shortcut("target")
