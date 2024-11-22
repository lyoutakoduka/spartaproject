#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_windows_head(identifier: str) -> Path:
    return Path(identifier.capitalize() + ":")


def build_windows_path(identifier: str, relative_root: Path) -> Path:
    return Path(get_windows_head(identifier), relative_root)
