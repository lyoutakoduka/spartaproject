#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get path about Windows file system."""

from pathlib import Path

from pyspartalib.script.path.modify.mount.build_windows_path import (
    get_windows_head,
    get_windows_path,
)


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_windows_head() -> Path:
    return get_windows_head(_get_drive_letter())


def _get_windows_path() -> Path:
    return get_windows_path(_get_drive_letter(), _get_relative_root())


def _get_expected_head() -> Path:
    return Path("C:")


def _get_expected_path() -> Path:
    return Path(_get_expected_head(), _get_relative_root())


def _compare_path(expected: Path, result: Path) -> None:
    assert expected == result


def test_head() -> None:
    """Test to get root path of drive about Windows file system."""
    _compare_path(_get_expected_head(), _get_windows_head())


def test_path() -> None:
    """Test to generate path about Windows file system from elements."""
    _compare_path(_get_expected_path(), _get_windows_path())
