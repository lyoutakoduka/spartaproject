#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.mount.shared.get_linux_head import (
    get_mount_point,
)


def _convert_linux(identifier: str) -> Path:
    return Path(get_mount_point(), identifier.lower())


def build_linux_path(identifier: str, relative_root: Path) -> Path:
    return Path(_convert_linux(identifier), relative_root)
