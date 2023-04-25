#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import raises
from pathlib import Path
from typing import List, Dict

from scripts.bools.same_value import bool_same_array
from scripts.paths.get_relative import path_relative, path_array_relative, path_pair_relative

_Strs = List[str]
_StrList = List[_Strs]
_Paths = List[Path]
_Pair = Dict[str, Path]
_PathPair = Dict[str, Path]


_BASE_PATH: Path = Path('project')
_HEAD_PATH: Path = Path(_BASE_PATH, 'sparta', 'tests', 'scripts', 'paths')

_TEST_PATH: _Strs = ['sparta', 'tests']
_EXPECTED: _StrList = [
    ['.'],
    ['sparta'],
    _TEST_PATH,
    _TEST_PATH + ['scripts'],
    _TEST_PATH + ['scripts', 'paths'],
]

_input_paths: _Paths = [
    Path(*_HEAD_PATH.parts[:i + 1])
    for i in range(len(_HEAD_PATH.parts))
]


def test_unmatch() -> None:
    with raises(ValueError):
        path_relative(_HEAD_PATH)


def test_single() -> None:
    assert _HEAD_PATH == path_relative(Path(__file__).parent)


def test_array() -> None:
    results: _Paths = path_array_relative(_input_paths, root_path=_BASE_PATH)
    expected: _Paths = [Path(*path_names) for path_names in _EXPECTED]

    assert expected == results


def test_pair() -> None:
    KEYS: _Strs = ['A', 'B', 'C', 'D', 'E']

    input_path_pair: _Pair = {
        key: path
        for key, path in zip(KEYS, _input_paths)
    }

    results: _PathPair = path_pair_relative(
        input_path_pair, root_path=_BASE_PATH)

    expected: _PathPair = {
        key: Path(*path_names)
        for key, path_names in zip(KEYS, _EXPECTED)
    }

    assert bool_same_array([results[key] == expected[key] for key in KEYS])


def main() -> bool:
    test_single()
    test_array()
    test_pair()
    return True
