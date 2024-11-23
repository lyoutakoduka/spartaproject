#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.mount.build_linux_path import (
    get_linux_head,
    get_linux_path,
)


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")


def _get_linux_head() -> Path:
    return get_linux_head(_get_drive_letter())


def _get_linux_path() -> Path:
    return get_linux_path(_get_drive_letter(), _get_relative_root())


def _get_expected_mount() -> Path:
    return Path("/", "mnt")
