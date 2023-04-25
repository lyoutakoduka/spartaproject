#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List, Dict

_Paths = List[Path]
_PathPair = Dict[str, Path]


def _default() -> Path:
    return Path.cwd()


def path_relative(absolute_path: Path, root_path: Path = _default()) -> Path:
    return absolute_path.relative_to(root_path)


def path_array_relative(absolute_paths: _Paths, root_path: Path = _default()) -> _Paths:
    return [path_relative(path, root_path) for path in absolute_paths]


def path_pair_relative(absolute_pair: _PathPair, root_path: Path = _default()) -> _PathPair:
    return {key: path_relative(path, root_path) for key, path in absolute_pair.items()}
