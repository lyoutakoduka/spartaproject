#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict, Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.bools.same_value import bool_same_array, bool_same_pair
from scripts.paths.check_exists import path_exists, path_array_exists, path_pair_exists
from scripts.paths.create_directory import path_mkdir, path_array_mkdir, path_pair_mkdir

_Strs = List[str]
_Paths = List[Path]
_PathPair = Dict[str, Path]

_ELEMENT_NAMES: _Strs = ['R', 'G', 'B']


def _get_head_path(index: int) -> Path:
    return Path(*[_ELEMENT_NAMES[i] for i in range(index + 1)])


def _inside_tmp_directory(func: Callable[[Path], bool]) -> None:
    with TemporaryDirectory() as tmp_path:
        assert func(Path(tmp_path))


def test_single() -> None:
    def make_dir(tmp_path: Path) -> bool:
        path: Path = Path(tmp_path, _ELEMENT_NAMES[0])
        path_mkdir(path)
        return path_exists(path)

    _inside_tmp_directory(make_dir)


def test_array() -> None:
    head_paths: _Paths = [
        _get_head_path(i)
        for i, _ in enumerate(_ELEMENT_NAMES)
    ]

    def make_dir(tmp_path: Path) -> bool:
        paths: _Paths = [
            Path(tmp_path, head_path)
            for head_path in head_paths
        ]
        path_array_mkdir(paths)
        return bool_same_array(path_array_exists(paths))

    _inside_tmp_directory(make_dir)


def test_pair() -> None:
    head_paths: _PathPair = {
        name: _get_head_path(i)
        for i, name in enumerate(_ELEMENT_NAMES)
    }

    def make_dir(tmp_path: Path) -> bool:
        paths: _PathPair = {
            name: Path(tmp_path, head_path)
            for name, head_path in head_paths.items()
        }
        path_pair_mkdir(paths)
        return bool_same_pair(path_pair_exists(paths))

    _inside_tmp_directory(make_dir)


def main() -> bool:
    test_single()
    test_array()
    test_pair()
    return True
