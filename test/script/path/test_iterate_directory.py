#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs, Strs2
from pyspartaproj.context.extension.path_context import PathGene, Paths
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative_array
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)

_tree_deep: int = 3

_name_dir_1: str = "dir001"
_name_dir_2: str = "dir002"
_name_dirs: Strs = [_name_dir_1, _name_dir_2]
_name_dir_empty: str = "empty"

_name_ini: str = "file.ini"
_name_json: str = "file.json"
_name_text: str = "file.txt"


def _sorted_match(expected: Paths, source: Paths) -> bool:
    return 1 == len(set([str(sorted(name)) for name in [expected, source]]))


def _check_walk_result(
    expected: Strs2, path_gene: PathGene, root_path: Path
) -> None:
    assert _sorted_match(
        [Path(*path_names) for path_names in expected],
        get_relative_array(list(path_gene), root_path=root_path),
    )


def _inside_temporary_directory(
    expected: Strs2, function: Callable[[Path], PathGene]
) -> None:
    with TemporaryDirectory() as temporary_path:
        root_path: Path = Path(temporary_path)
        create_temporary_tree(root_path, tree_deep=_tree_deep)
        _check_walk_result(expected, function(root_path), root_path)


def test_all() -> None:
    expected: Strs2 = [
        [_name_dir_1],
        [_name_dir_empty],
        [_name_ini],
        [_name_json],
        [_name_text],
        _name_dirs,
        [_name_dir_1, _name_dir_empty],
        [_name_dir_1, _name_ini],
        [_name_dir_1, _name_json],
        [_name_dir_1, _name_text],
        _name_dirs + [_name_dir_empty],
        _name_dirs + [_name_ini],
        _name_dirs + [_name_json],
        _name_dirs + [_name_text],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path)

    _inside_temporary_directory(expected, individual_test)


def test_depth() -> None:
    expected: Strs2 = [
        _name_dirs,
        [_name_dir_1, _name_dir_empty],
        [_name_dir_1, _name_ini],
        [_name_dir_1, _name_json],
        [_name_dir_1, _name_text],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, depth=2)

    _inside_temporary_directory(expected, individual_test)


def test_directory() -> None:
    expected: Strs2 = [
        [_name_ini],
        [_name_json],
        [_name_text],
        [_name_dir_1, _name_ini],
        [_name_dir_1, _name_json],
        [_name_dir_1, _name_text],
        _name_dirs + [_name_ini],
        _name_dirs + [_name_json],
        _name_dirs + [_name_text],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, directory=False)

    _inside_temporary_directory(expected, individual_test)


def test_file() -> None:
    expected: Strs2 = [
        [_name_dir_1],
        [_name_dir_empty],
        _name_dirs,
        [_name_dir_1, _name_dir_empty],
        _name_dirs + [_name_dir_empty],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, file=False)

    _inside_temporary_directory(expected, individual_test)


def test_suffix() -> None:
    expected: Strs2 = [
        [_name_json],
        [_name_dir_1, _name_json],
        _name_dirs + [_name_json],
    ]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, directory=False, suffix="json")

    _inside_temporary_directory(expected, individual_test)


def test_filter() -> None:
    expected: Strs2 = [_name_dirs + [_name_text]]

    def individual_test(root_path: Path) -> PathGene:
        return walk_iterator(root_path, glob_filter="*/*/*.txt")

    _inside_temporary_directory(expected, individual_test)


def main() -> bool:
    test_all()
    test_depth()
    test_directory()
    test_file()
    test_suffix()
    test_filter()
    return True
