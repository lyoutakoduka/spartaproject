#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

_Paths = List[Path]


def path_absolute(relative_path: Path) -> Path:
    return relative_path.absolute()  # resolve() ignore symbolic link


def path_array_absolute(relative_paths: _Paths) -> _Paths:
    return [path_absolute(path) for path in relative_paths]
