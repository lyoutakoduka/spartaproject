#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.default.bool_context import Bools, BoolPair
from context.extension.path_context import Path, Paths, PathPair
from script.bool.compare_value import bool_compare_array, bool_compare_pair
from script.path.check_exists import check_exists_array, check_exists_pair
from script.path.modify.get_absolute import (
    get_absolute, get_absolute_array, get_absolute_pair
)


_BASE_PATH: Path = Path('project', 'sparta')
_EMPTY_HEAD: Path = Path('script', 'debug_empty.py')
_EMPTY_PATH: Path = Path(_BASE_PATH, _EMPTY_HEAD)


def test_ignore() -> None:
    path: Path = Path(__file__)
    assert path == get_absolute(path)


def test_single() -> None:
    expected: Path = Path(__file__)

    current: Path = Path.cwd()
    expected_text: str = expected.as_posix()
    input: Path = Path(expected_text[len(current.as_posix()) + 1:])

    assert expected == get_absolute(input)


def test_root() -> None:
    expected: Path = Path(__file__)

    assert expected == get_absolute(
        Path(expected.name), root_path=expected.parent
    )


def test_array() -> None:
    RELATIVE_PATHS: Paths = [_BASE_PATH, _EMPTY_HEAD]
    EXPECTS: Bools = [True, False]

    absolute_paths: Paths = get_absolute_array(RELATIVE_PATHS)
    assert bool_compare_array(EXPECTS, check_exists_array(absolute_paths))


def test_pair() -> None:
    RELATIVE_PATHS: PathPair = {
        'R': _EMPTY_PATH, 'G': _EMPTY_HEAD, 'B': _EMPTY_PATH
    }
    EXPECTS: BoolPair = {'R': True, 'G': False, 'B': True}

    absolute_paths: PathPair = get_absolute_pair(RELATIVE_PATHS)
    assert bool_compare_pair(EXPECTS, check_exists_pair(absolute_paths))


def main() -> bool:
    test_ignore()
    test_single()
    test_root()
    test_array()
    test_pair()
    return True
