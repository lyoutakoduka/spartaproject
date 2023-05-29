#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import raises

from context.path_context import Path, Paths, PathPair
from context.default.string_context import Strs, Strs2
from script.bool.same_value import bool_same_array
from script.path.get_relative import (
    get_relative, get_relative_array, get_relative_pair
)


_BASE_PATH: Path = Path('project')
_HEAD_PATH: Path = Path(_BASE_PATH, 'sparta', 'test', 'script', 'path')

_TEST_PATH: Strs = ['sparta', 'test']
_EXPECTED: Strs2 = [
    ['.'],
    ['sparta'],
    _TEST_PATH,
    _TEST_PATH + ['script'],
    _TEST_PATH + ['script', 'path'],
]

_input_paths: Paths = [
    Path(*_HEAD_PATH.parts[:i + 1]) for i in range(len(_HEAD_PATH.parts))
]


def test_unmatch() -> None:
    with raises(ValueError):
        get_relative(_HEAD_PATH)


def test_single() -> None:
    assert _HEAD_PATH == get_relative(Path(__file__).parent)


def test_array() -> None:
    results: Paths = get_relative_array(_input_paths, root_path=_BASE_PATH)
    expected: Paths = [Path(*path_names) for path_names in _EXPECTED]

    assert expected == results


def test_pair() -> None:
    KEYS: Strs = ['A', 'B', 'C', 'D', 'E']

    results: PathPair = get_relative_pair(
        {key: path for key, path in zip(KEYS, _input_paths)},
        root_path=_BASE_PATH,
    )

    expected: PathPair = {
        key: Path(*path_names) for key, path_names in zip(KEYS, _EXPECTED)
    }

    assert bool_same_array([results[key] == expected[key] for key in KEYS])


def main() -> bool:
    test_single()
    test_array()
    test_pair()
    return True
