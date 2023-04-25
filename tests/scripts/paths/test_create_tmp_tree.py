#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from sparta.scripts.paths.get_relative import path_array_relative
from sparta.scripts.paths.create_tmp_tree import create_tree
from sparta.scripts.paths.iterate_directory import walk_iterator

_Ints = List[int]
_Strs = List[str]
_Paths = List[Path]
_StrList = List[_Strs]


def _inside_tmp_directory(func: Callable[[Path], None]) -> _Paths:
    with TemporaryDirectory() as tmp_path:
        root_path: Path = Path(tmp_path)
        func(root_path)
        return path_array_relative(list(walk_iterator(root_path)), root_path=root_path)


def test_three() -> None:
    NAME_DIR_1: str = 'dir001'
    NAME_DIR_2: str = 'dir002'
    NAME_DIRS: _Strs = [NAME_DIR_1, NAME_DIR_2]
    NAME_DIR_EMPTY: str = 'empty'

    NAME_INI: str = 'file.ini'
    NAME_JSON: str = 'file.json'
    NAME_TEXT: str = 'file.txt'

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

    expected: _Paths = [Path(*path_names) for path_names in EXPECTED]

    def make_tree(tmp_path: Path) -> None:
        create_tree(tmp_path, tree_deep=3)

    assert expected == _inside_tmp_directory(make_tree)


def test_empty() -> None:
    OUTRANGE_INDICES: _Ints = [-2, -1, 0, 11, 12, 13]

    def make_tree(tmp_path: Path) -> None:
        for index in OUTRANGE_INDICES:
            create_tree(tmp_path, tree_deep=index)

    assert 0 == len(_inside_tmp_directory(make_tree))


def main() -> bool:
    test_three()
    test_empty()
    return True
