#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools, BoolPair
from contexts.path_context import Path, Paths, PathPair
from scripts.bools.compare_value import bool_compare_array, bool_compare_pair
from scripts.paths.check_exists import path_array_exists, path_pair_exists

_CURRENT_PATH: Path = Path(__file__)
_UNKNOWN_PATH: Path = _CURRENT_PATH.with_name('unknown.py')


def test_array() -> None:
    PATHS: Paths = [_CURRENT_PATH, _UNKNOWN_PATH]
    EXPECTS: Bools = [True, False]

    assert bool_compare_array(EXPECTS, path_array_exists(PATHS))


def test_pair() -> None:
    PATHS: PathPair = {
        'R': _CURRENT_PATH,
        'G': _UNKNOWN_PATH,
        'B': _CURRENT_PATH.parent,
    }
    EXPECTS: BoolPair = {'R': True, 'G': False, 'B': True}

    assert bool_compare_pair(EXPECTS, path_pair_exists(PATHS))


def main() -> bool:
    test_array()
    test_pair()
    return True
