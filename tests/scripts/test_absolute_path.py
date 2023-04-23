#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.same_elements import all_true
from scripts.path_exists import check_paths, check_path
from scripts.absolute_path import convert_paths, convert_path

_Paths = List[Path]

_BASE_PATH: Path = Path('project', 'sparta')
_EMPTY_PATH: Path = _BASE_PATH.joinpath('scripts', 'debug_empty.py')


def test_ignore() -> None:
    path: Path = Path(__file__)
    assert path == convert_path(path)


def test_single() -> None:
    assert check_path(convert_path(_EMPTY_PATH))


def test_multi() -> None:
    RELATIVE_PATH: _Paths = [
        _EMPTY_PATH,
        _BASE_PATH.joinpath('debug_wrapper.py'),
    ]

    assert all_true(check_paths(convert_paths(RELATIVE_PATH)))


def main() -> bool:
    test_ignore()
    test_single()
    test_multi()
    return True
