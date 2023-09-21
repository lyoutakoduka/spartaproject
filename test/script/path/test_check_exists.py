#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from spartaproject.context.default.bool_context import BoolPair, Bools
from spartaproject.context.extension.path_context import PathPair, Paths
from spartaproject.script.bool.compare_value import (bool_compare_array,
                                                     bool_compare_pair)
from spartaproject.script.path.check_exists import (check_exists_array,
                                                    check_exists_pair)

_CURRENT_PATH: Path = Path(__file__)
_UNKNOWN_PATH: Path = _CURRENT_PATH.with_name('unknown.py')


def test_array() -> None:
    PATHS: Paths = [_CURRENT_PATH, _UNKNOWN_PATH]
    EXPECTED: Bools = [True, False]

    assert bool_compare_array(EXPECTED, check_exists_array(PATHS))


def test_pair() -> None:
    PATHS: PathPair = {
        'R': _CURRENT_PATH, 'G': _UNKNOWN_PATH, 'B': _CURRENT_PATH.parent
    }
    EXPECTED: BoolPair = {'R': True, 'G': False, 'B': True}

    assert bool_compare_pair(EXPECTED, check_exists_pair(PATHS))


def main() -> bool:
    test_array()
    test_pair()
    return True
