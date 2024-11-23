#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.mount.build_windows_path import (
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
