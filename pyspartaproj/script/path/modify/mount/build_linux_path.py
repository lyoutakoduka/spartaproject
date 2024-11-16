#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.mount.get_linux_head import get_linux_head


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _convert_linux(identifier: str) -> Path:
    return Path(get_linux_head(), identifier.lower())


def build_linux_path(identifier: str, relative_root: Path) -> Path:
    return Path(_convert_linux(identifier), relative_root)
