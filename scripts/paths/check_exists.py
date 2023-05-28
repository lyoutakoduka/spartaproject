#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.defaults.bool_context import Bools, BoolPair
from context.path_context import Path, Paths, PathPair


def _check_exists(path: Path) -> bool:
    return path.exists()


def check_exists_array(paths: Paths) -> Bools:
    return [_check_exists(path) for path in paths]


def check_exists_pair(paths: PathPair) -> BoolPair:
    return {key: _check_exists(path) for key, path in paths.items()}
