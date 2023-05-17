#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from contexts.path_context import Path, Paths, PathGene
from contexts.string_context import Strs, Strs2
from scripts.paths.create_tmp_tree import create_tree
from scripts.paths.get_relative import path_array_relative
from scripts.paths.iterate_directory import walk_iterator

_TREE_DEEP: int = 3

_NAME_DIR_1: str = 'dir001'
_NAME_DIR_2: str = 'dir002'
_NAME_DIRS: Strs = [_NAME_DIR_1, _NAME_DIR_2]
_NAME_DIR_EMPTY: str = 'empty'

_NAME_INI: str = 'file.ini'
_NAME_JSON: str = 'file.json'
_NAME_TEXT: str = 'file.txt'


def _check_walk_result(expected: Strs2, path_gene: PathGene, root_path: Path) -> None:
    results: Paths = path_array_relative(list(path_gene), root_path=root_path)
    expected_paths: Paths = [Path(*path_names) for path_names in expected]

    assert expected_paths == results


def _inside_tmp_directory(expected: Strs2, func: Callable[[Path], PathGene]) -> None:
    with TemporaryDirectory() as tmp_path:
        root_path: Path = Path(tmp_path)
        create_tree(root_path, tree_deep=_TREE_DEEP)
        _check_walk_result(expected, func(root_path), root_path)


def test_all() -> None:
    EXPECTED: Strs2 = [
        [_NAME_DIR_1],
        [_NAME_DIR_EMPTY],
        [_NAME_INI],
        [_NAME_JSON],
        [_NAME_TEXT],
        _NAME_DIRS,
        [_NAME_DIR_1, _NAME_DIR_EMPTY],
        [_NAME_DIR_1, _NAME_INI],
        [_NAME_DIR_1, _NAME_JSON],
        [_NAME_DIR_1, _NAME_TEXT],
        _NAME_DIRS + [_NAME_DIR_EMPTY],
        _NAME_DIRS + [_NAME_INI],
        _NAME_DIRS + [_NAME_JSON],
        _NAME_DIRS + [_NAME_TEXT],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path)
    _inside_tmp_directory(EXPECTED, individual_test)


def test_depth() -> None:
    EXPECTED: Strs2 = [
        _NAME_DIRS,
        [_NAME_DIR_1, _NAME_DIR_EMPTY],
        [_NAME_DIR_1, _NAME_INI],
        [_NAME_DIR_1, _NAME_JSON],
        [_NAME_DIR_1, _NAME_TEXT],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, depth=2)
    _inside_tmp_directory(EXPECTED, individual_test)


def test_directory() -> None:
    EXPECTED: Strs2 = [
        [_NAME_INI],
        [_NAME_JSON],
        [_NAME_TEXT],
        [_NAME_DIR_1, _NAME_INI],
        [_NAME_DIR_1, _NAME_JSON],
        [_NAME_DIR_1, _NAME_TEXT],
        _NAME_DIRS + [_NAME_INI],
        _NAME_DIRS + [_NAME_JSON],
        _NAME_DIRS + [_NAME_TEXT],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, directory=False)
    _inside_tmp_directory(EXPECTED, individual_test)


def test_file() -> None:
    EXPECTED: Strs2 = [
        [_NAME_DIR_1],
        [_NAME_DIR_EMPTY],
        _NAME_DIRS,
        [_NAME_DIR_1, _NAME_DIR_EMPTY],
        _NAME_DIRS + [_NAME_DIR_EMPTY],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, file=False)
    _inside_tmp_directory(EXPECTED, individual_test)


def test_suffix() -> None:
    EXPECTED: Strs2 = [
        [_NAME_JSON],
        [_NAME_DIR_1, _NAME_JSON],
        _NAME_DIRS + [_NAME_JSON],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, directory=False, suffix='json')
    _inside_tmp_directory(EXPECTED, individual_test)


def test_filter() -> None:
    EXPECTED: Strs2 = [_NAME_DIRS + [_NAME_TEXT]]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, filter='*/*/*.txt')
    _inside_tmp_directory(EXPECTED, individual_test)


def main() -> bool:
    test_all()
    test_depth()
    test_directory()
    test_file()
    test_suffix()
    test_filter()
    return True
