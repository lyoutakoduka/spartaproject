#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import raises

from context.default.string_context import Strs, Strs2
from context.extension.path_context import Path, Paths, PathPair
from script.bool.same_value import bool_same_array
from script.path.modify.get_absolute import (
    get_absolute, get_absolute_array
)
from script.path.modify.get_relative import (
    get_relative, get_relative_array, get_relative_pair
)


_BASE_PATH: Path = Path('project')
_HEAD_PATH: Path = Path(
    _BASE_PATH, 'sparta', 'test', 'script', 'path', 'modify'
)

_TEST_PATH: Strs = ['sparta', 'test']
_EXPECTED: Strs2 = [
    ['.'],
    ['sparta'],
    _TEST_PATH,
    _TEST_PATH + ['script'],
    _TEST_PATH + ['script', 'path'],
    _TEST_PATH + ['script', 'path', 'modify']
]

_input_paths: Paths = [
    Path(*_HEAD_PATH.parts[:i + 1]) for i in range(len(_HEAD_PATH.parts))
]


def test_unmatch() -> None:
    with raises(ValueError):
        get_relative(Path('empty'))


def test_single() -> None:
    expected: Path = Path(__file__)
    assert expected == get_absolute(get_relative(expected))


def test_array() -> None:
    current: Path = Path(__file__)
    expected: Paths = [current.parents[i] for i in range(3)]
    assert expected == get_absolute_array(get_relative_array(expected))


def test_pair() -> None:
    KEYS: Strs = ['A', 'B', 'C', 'D', 'E']

    results: PathPair = get_relative_pair(
        {key: path for key, path in zip(KEYS, _input_paths)},
        root_path=_BASE_PATH
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
