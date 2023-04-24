#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict
from pathlib import Path

_Paths = List[Path]
_PathPair = Dict[str, Path]


def path_mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def path_array_mkdir(paths: _Paths) -> None:
    for path in paths:
        path_mkdir(path)


def path_pair_mkdir(path_pair: _PathPair) -> None:
    for _, path in path_pair.items():
        path_mkdir(path)
