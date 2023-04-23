#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.same_elements import all_true
from scripts.path_exists import check_paths, check_path
from scripts.absolute_path import convert_paths, convert_path

_Strs = List[str]
_Bools = List[bool]
_StrsList = List[_Strs]

_BASE_PATH: _Strs = ['project', 'sparta']
_EMPTY_PATH: _Strs = _BASE_PATH + ['scripts', 'debug_empty.py']


def test_full() -> None:
    path: str = __file__
    assert path == convert_path(path)


def test_single() -> None:
    absolute_path: str = convert_path(str(Path(*_EMPTY_PATH)))

    assert check_path(absolute_path)


def test_multi() -> None:
    RELATIVE_PATH: _StrsList = [
        _EMPTY_PATH,
        _BASE_PATH + ['debug_wrapper.py']
    ]

    relative_paths: _Strs = [
        str(Path(*relative_path))
        for relative_path in RELATIVE_PATH
    ]

    absolute_paths: _Strs = convert_paths(relative_paths)
    file_exists: _Bools = check_paths(absolute_paths)

    assert all_true(file_exists)


def main() -> bool:
    test_full()
    test_single()
    test_multi()
    return True
