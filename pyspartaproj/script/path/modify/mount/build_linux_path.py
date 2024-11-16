#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _get_mount_root() -> Path:
    return Path("/", "mnt")


def _convert_linux(identifier: str) -> Path:
    return Path(_get_mount_root(), identifier.lower())
