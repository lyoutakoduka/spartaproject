#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.same_elements import all_true
from scripts.path_exists import check_paths, check_path
from scripts.absolute_path import convert_paths, convert_path

_Strs = List[str]
_StrsList = List[_Strs]

_BASE_PATH: _Strs = ['project', 'sparta']
_EMPTY_PATH: _Strs = _BASE_PATH + ['scripts', 'debug_empty.py']


def test_full() -> None:
    path: str = __file__
    assert path == convert_path(path)


def test_single() -> None:
    assert check_path(convert_path(str(Path(*_EMPTY_PATH))))


def test_multi() -> None:
    RELATIVE_PATH: _StrsList = [
        _EMPTY_PATH,
        _BASE_PATH + ['debug_wrapper.py']
    ]

    relative_paths: _Strs = [
        str(Path(*relative_path))
        for relative_path in RELATIVE_PATH
    ]

    assert all_true(check_paths(convert_paths(relative_paths)))


def main() -> bool:
    test_full()
    test_single()
    test_multi()
    return True
