#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.mount.build_linux_path import (
    build_linux_path,
)


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_expected_path() -> Path:
    return Path(_get_drive_letter(), _get_relative_root())


def _get_linux_path() -> Path:
    return build_linux_path(_get_drive_letter(), _get_relative_root())
