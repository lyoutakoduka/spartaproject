#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

_Paths = List[Path]


def convert_path(relative_path: Path) -> Path:
    return relative_path.absolute()  # resolve() ignore symbolic link


def convert_paths(relative_paths: _Paths) -> _Paths:
    return [convert_path(path) for path in relative_paths]
