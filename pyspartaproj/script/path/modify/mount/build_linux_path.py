#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _convert_linux(identifier: str) -> Path:
    return Path(_get_mount_root(), identifier.lower())


def build_linux_path(identifier: str, relative_root: Path) -> Path:
    return Path(_convert_linux(identifier), relative_root)
