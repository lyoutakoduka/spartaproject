#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List, Dict

_Paths = List[Path]
_Bools = List[bool]
_PathPair = Dict[str, Path]
_BoolPair = Dict[str, bool]


def path_exists(path: Path) -> bool:
    return Path(path).exists()


def path_array_exists(paths: _Paths) -> _Bools:
    return [path_exists(path) for path in paths]


def path_pair_exists(paths: _PathPair) -> _BoolPair:
    return {key: path_exists(path) for key, path in paths.items()}
