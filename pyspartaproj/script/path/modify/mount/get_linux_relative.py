#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import get_relative


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def get_linux_relative(path: Path) -> Path:
    return get_relative(path, root_path=_get_mount_root())
