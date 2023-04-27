#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools, BoolPair
from contexts.path_context import Path, Paths, PathPair


def path_exists(path: Path) -> bool:
    return Path(path).exists()


def path_array_exists(paths: Paths) -> Bools:
    return [path_exists(path) for path in paths]


def path_pair_exists(paths: PathPair) -> BoolPair:
    return {key: path_exists(path) for key, path in paths.items()}
