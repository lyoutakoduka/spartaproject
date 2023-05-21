#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools, BoolPair
from contexts.path_context import Path, Paths, PathPair
from scripts.bools.compare_value import bool_compare_array, bool_compare_pair
from scripts.paths.check_exists import (
    path_exists, path_array_exists, path_pair_exists
)
from scripts.paths.get_absolute import (
    path_absolute, path_array_absolute, path_pair_absolute
)


_BASE_PATH: Path = Path('project', 'sparta')
_EMPTY_HEAD: Path = Path('scripts', 'debug_empty.py')
_EMPTY_PATH: Path = Path(_BASE_PATH, _EMPTY_HEAD)


def test_ignore() -> None:
    path: Path = Path(__file__)
    assert path == path_absolute(path)


def test_single() -> None:
    assert path_exists(path_absolute(_EMPTY_PATH))


def test_array() -> None:
    RELATIVE_PATHS: Paths = [_BASE_PATH, _EMPTY_HEAD]
    EXPECTS: Bools = [True, False]

    absolute_paths: Paths = path_array_absolute(RELATIVE_PATHS)
    assert bool_compare_array(EXPECTS, path_array_exists(absolute_paths))


def test_pair() -> None:
    RELATIVE_PATHS: PathPair = {
        'R': _EMPTY_PATH,
        'G': _EMPTY_HEAD,
        'B': _EMPTY_PATH,
    }
    EXPECTS: BoolPair = {'R': True, 'G': False, 'B': True}

    absolute_paths: PathPair = path_pair_absolute(RELATIVE_PATHS)
    assert bool_compare_pair(EXPECTS, path_pair_exists(absolute_paths))


def main() -> bool:
    test_ignore()
    test_single()
    test_array()
    test_pair()
    return True
