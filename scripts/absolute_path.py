#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

_Strs = List[str]


def convert_path(relative_path: str) -> str:
    path: Path = Path(relative_path)
    return str(path.absolute())  # resolve() ignore symbolic link


def convert_paths(relative_paths: _Strs) -> _Strs:
    return [convert_path(path) for path in relative_paths]
