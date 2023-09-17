#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.default.bool_context import BoolPair, Bools
from context.extension.path_context import Path, PathPair, Paths


def _check_exists(path: Path) -> bool:
    return path.exists()


def check_exists_array(paths: Paths) -> Bools:
    return [_check_exists(path) for path in paths]


def check_exists_pair(paths: PathPair) -> BoolPair:
    return {key: _check_exists(path) for key, path in paths.items()}
