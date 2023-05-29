#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.default.bool_context import Bools, BoolPair
from context.extension.path_context import Path, Paths, PathPair
from script.bool.compare_value import bool_compare_array, bool_compare_pair
from script.path.check_exists import check_exists_array, check_exists_pair

_CURRENT_PATH: Path = Path(__file__)
_UNKNOWN_PATH: Path = _CURRENT_PATH.with_name('unknown.py')


def test_array() -> None:
    PATHS: Paths = [_CURRENT_PATH, _UNKNOWN_PATH]
    EXPECTS: Bools = [True, False]

    assert bool_compare_array(EXPECTS, check_exists_array(PATHS))


def test_pair() -> None:
    PATHS: PathPair = {
        'R': _CURRENT_PATH, 'G': _UNKNOWN_PATH, 'B': _CURRENT_PATH.parent
    }
    EXPECTS: BoolPair = {'R': True, 'G': False, 'B': True}

    assert bool_compare_pair(EXPECTS, check_exists_pair(PATHS))


def main() -> bool:
    test_array()
    test_pair()
    return True
