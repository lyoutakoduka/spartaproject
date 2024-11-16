#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _convert_windows(identifier: str) -> Path:
    return Path(identifier.capitalize() + ":")


def build_windows_path(identifier: str, relative_root: Path) -> Path:
    return Path(_convert_windows(identifier), relative_root)
