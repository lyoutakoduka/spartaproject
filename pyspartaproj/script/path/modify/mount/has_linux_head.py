#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import is_relative


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def has_linux_head(path: Path) -> bool:
    return is_relative(path, root_path=_get_mount_root())
