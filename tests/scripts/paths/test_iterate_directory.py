#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Callable, Generator
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.paths.get_relative import path_array_relative
from scripts.paths.create_tmp_tree import create_tree
from scripts.paths.iterate_directory import walk_iterator

_Paths = List[Path]
_Strs = List[str]
_StrList = List[_Strs]
_PathGene = Generator[Path, None, None]

TREE_DEEP: int = 3

NAME_DIR_1: str = 'dir001'
NAME_DIR_2: str = 'dir002'
NAME_DIRS: _Strs = [NAME_DIR_1, NAME_DIR_2]
NAME_DIR_EMPTY: str = 'empty'

NAME_INI: str = 'file.ini'
NAME_JSON: str = 'file.json'
NAME_TEXT: str = 'file.txt'


def _check_walk_result(expected: _StrList, path_gene: _PathGene, root_path: Path) -> None:
    results: _Paths = path_array_relative(list(path_gene), root_path=root_path)
    expected_paths: _Paths = [Path(*path_names) for path_names in expected]

    assert expected_paths == results


def _inside_tmp_directory(expected: _StrList, func: Callable[[Path], _PathGene]) -> None:
    with TemporaryDirectory() as tmp_path:
        root_path: Path = Path(tmp_path)
        create_tree(root_path, tree_deep=TREE_DEEP)
        _check_walk_result(expected, func(root_path), root_path)


def test_all() -> None:
    EXPECTED: _StrList = [
        [NAME_DIR_1],
        [NAME_DIR_EMPTY],
        [NAME_INI],
        [NAME_JSON],
        [NAME_TEXT],
        NAME_DIRS,
        [NAME_DIR_1, NAME_DIR_EMPTY],
        [NAME_DIR_1, NAME_INI],
        [NAME_DIR_1, NAME_JSON],
        [NAME_DIR_1, NAME_TEXT],
        NAME_DIRS + [NAME_DIR_EMPTY],
        NAME_DIRS + [NAME_INI],
        NAME_DIRS + [NAME_JSON],
        NAME_DIRS + [NAME_TEXT],
    ]

    def make_tree(root_path: Path) -> _PathGene:
        return walk_iterator(root_path)
    _inside_tmp_directory(EXPECTED, make_tree)


def test_depth() -> None:
    EXPECTED: _StrList = [
        NAME_DIRS + [NAME_DIR_EMPTY],
        NAME_DIRS + [NAME_INI],
        NAME_DIRS + [NAME_JSON],
        NAME_DIRS + [NAME_TEXT],
    ]

    def make_tree(root_path: Path) -> _PathGene:
        return walk_iterator(root_path, depth=2)
    _inside_tmp_directory(EXPECTED, make_tree)


def test_directory() -> None:
    EXPECTED: _StrList = [
        [NAME_INI],
        [NAME_JSON],
        [NAME_TEXT],
        [NAME_DIR_1, NAME_INI],
        [NAME_DIR_1, NAME_JSON],
        [NAME_DIR_1, NAME_TEXT],
        NAME_DIRS + [NAME_INI],
        NAME_DIRS + [NAME_JSON],
        NAME_DIRS + [NAME_TEXT],
    ]

    def make_tree(root_path: Path) -> _PathGene:
        return walk_iterator(root_path, directory=False)
    _inside_tmp_directory(EXPECTED, make_tree)


def test_file() -> None:
    EXPECTED: _StrList = [
        [NAME_DIR_1],
        NAME_DIRS,
        NAME_DIRS + [NAME_DIR_EMPTY],
        [NAME_DIR_1, NAME_DIR_EMPTY],
        [NAME_DIR_EMPTY],
    ]

    def make_tree(root_path: Path) -> _PathGene:
        return walk_iterator(root_path, file=False)
    _inside_tmp_directory(EXPECTED, make_tree)


def test_suffix() -> None:
    EXPECTED: _StrList = [
        [NAME_JSON],
        [NAME_DIR_1, NAME_JSON],
        NAME_DIRS + [NAME_JSON],
    ]

    def make_tree(root_path: Path) -> _PathGene:
        return walk_iterator(root_path, directory=False, suffix='json')
    _inside_tmp_directory(EXPECTED, make_tree)


def test_filter() -> None:
    EXPECTED: _StrList = [NAME_DIRS + [NAME_TEXT]]

    def make_tree(root_path: Path) -> _PathGene:
        return walk_iterator(root_path, filter='*/*/*.txt')
    _inside_tmp_directory(EXPECTED, make_tree)


def main() -> bool:
    test_all()
    test_depth()
    test_directory()
    test_file()
    test_suffix()
    test_filter()
    return True
