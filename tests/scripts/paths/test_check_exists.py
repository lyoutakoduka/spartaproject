#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List, Dict

from scripts.bools.compare_value import bool_compare_array, bool_compare_pair
from scripts.paths.check_exists import path_exists, path_array_exists, path_pair_exists

_Bools = List[bool]
_BoolPair = Dict[str, bool]
_Paths = List[Path]
_PathPair = Dict[str, Path]

CURRENT_PATH: Path = Path(__file__)
UNKNOWN_PATH: Path = CURRENT_PATH.with_name('unknown.py')


def test_single() -> None:
    assert path_exists(CURRENT_PATH)


def test_array() -> None:
    PATHS: _Paths = [
        CURRENT_PATH,
        UNKNOWN_PATH
    ]
    EXPECTS: _Bools = [True, False]

    assert bool_compare_array(EXPECTS, path_array_exists(PATHS))


def test_pair() -> None:
    PATHS: _PathPair = {
        'R': CURRENT_PATH,
        'G': UNKNOWN_PATH,
        'B': CURRENT_PATH.parent,
    }
    EXPECTS: _BoolPair = {'R': True, 'G': False, 'B': True}

    assert bool_compare_pair(EXPECTS, path_pair_exists(PATHS))


def main() -> bool:
    test_single()
    test_array()
    test_pair()
    return True
