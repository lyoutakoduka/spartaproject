#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.bools.same_array import bool_same_array
from scripts.paths.check_exists import path_array_exists, path_exists
from scripts.paths.get_absolute import path_array_absolute, path_absolute

_Paths = List[Path]

_BASE_PATH: Path = Path('project', 'sparta')
_EMPTY_PATH: Path = _BASE_PATH.joinpath('scripts', 'debug_empty.py')


def test_ignore() -> None:
    path: Path = Path(__file__)
    assert path == path_absolute(path)


def test_single() -> None:
    assert path_exists(path_absolute(_EMPTY_PATH))


def test_multi() -> None:
    RELATIVE_PATH: _Paths = [
        _EMPTY_PATH,
        _BASE_PATH.joinpath('debug_wrapper.py'),
    ]

    assert bool_same_array(
        path_array_exists(
            path_array_absolute(RELATIVE_PATH)))


def main() -> bool:
    test_ignore()
    test_single()
    test_multi()
    return True
