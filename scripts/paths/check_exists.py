#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools, BoolPair
from contexts.path_context import Path, Paths, PathPair


def _exists(path: Path) -> bool:
    return path.exists()


def path_array_exists(paths: Paths) -> Bools:
    return [_exists(path) for path in paths]


def path_pair_exists(paths: PathPair) -> BoolPair:
    return {key: _exists(path) for key, path in paths.items()}
