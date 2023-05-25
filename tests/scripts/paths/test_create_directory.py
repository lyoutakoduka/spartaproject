#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from contexts.path_context import Path, Paths, PathPair
from contexts.string_context import Strs
from scripts.bools.same_value import bool_same_array, bool_same_pair
from scripts.paths.check_exists import path_array_exists, path_pair_exists
from scripts.paths.create_directory import (
    path_mkdir, path_array_mkdir, path_pair_mkdir
)

_ELEMENT_NAMES: Strs = ['R', 'G', 'B']


def _get_head_path(index: int) -> Path:
    return Path(*[_ELEMENT_NAMES[i] for i in range(index + 1)])


def _inside_tmp_directory(func: Callable[[Path], bool]) -> None:
    with TemporaryDirectory() as tmp_path:
        assert func(Path(tmp_path))


def test_single() -> None:
    def individual_test(tmp_path: Path) -> bool:
        return path_mkdir(Path(tmp_path, _ELEMENT_NAMES[0])).exists()

    _inside_tmp_directory(individual_test)


def test_array() -> None:
    head_paths: Paths = [
        _get_head_path(i) for i, _ in enumerate(_ELEMENT_NAMES)
    ]

    def individual_test(tmp_path: Path) -> bool:
        paths: Paths = [Path(tmp_path, head_path) for head_path in head_paths]

        return bool_same_array(path_array_exists(path_array_mkdir(paths)))

    _inside_tmp_directory(individual_test)


def test_pair() -> None:
    head_paths: PathPair = {
        name: _get_head_path(i) for i, name in enumerate(_ELEMENT_NAMES)
    }

    def individual_test(tmp_path: Path) -> bool:
        paths: PathPair = {
            name: Path(tmp_path, head_path)
            for name, head_path in head_paths.items()
        }

        return bool_same_pair(path_pair_exists(path_pair_mkdir(paths)))

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_single()
    test_array()
    test_pair()
    return True
