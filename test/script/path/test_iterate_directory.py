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
_name_dir_empty: str = "empty"
_name_ini: str = "file.ini"
_name_json: str = "file.json"
_name_text: str = "file.txt"


def _get_first_ini() -> Strs:
    return [_name_ini]


def _get_first_json() -> Strs:
    return [_name_json]


def _get_first_text() -> Strs:
    return [_name_text]


def _get_first_empty() -> Strs:
    return [_name_dir_empty]


def _get_first_files() -> Strs2:
    return [_get_first_ini(), _get_first_json(), _get_first_text()]


def _get_second_root() -> Strs:
    return [_name_dir_1]


def _get_second_ini() -> Strs:
    return _get_second_root() + _get_first_ini()


def _get_second_json() -> Strs:
    return _get_second_root() + _get_first_json()


def _get_second_text() -> Strs:
    return _get_second_root() + _get_first_text()


def _get_second_empty() -> Strs:
    return _get_second_root() + _get_first_empty()


def _get_second_files() -> Strs2:
    return [
        _get_second_ini(),
        _get_second_json(),
        _get_second_text(),
    ]


def _get_third_root() -> Strs:
    return _get_second_root() + [_name_dir_2]


def _get_third_text() -> Strs:
    return _get_third_root() + _get_first_text()


def _get_third_ini() -> Strs:
    return _get_third_root() + _get_first_ini()


def _get_third_json() -> Strs:
    return _get_third_root() + _get_first_json()


def _get_third_empty() -> Strs:
    return _get_third_root() + _get_first_empty()


def _get_third_files() -> Strs2:
    return [
        _get_third_ini(),
        _get_third_json(),
        _get_third_text(),
    ]


def _sorted_match(expected: Paths, source: Paths) -> bool:
    return 1 == len(set([str(sorted(name)) for name in [expected, source]]))


def _common_test(
    expected: Strs2, path_gene: PathGene, root_path: Path
) -> None:
    assert _sorted_match(
        [Path(*path_names) for path_names in expected],
        get_relative_array(list(path_gene), root_path=root_path),
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(
            create_temporary_tree(Path(temporary_path), tree_deep=_tree_deep)
        )


def test_all() -> None:
    expected: Strs2 = [
        _get_first_empty(),
        *_get_first_files(),
        _get_second_root(),
        _get_second_empty(),
        *_get_second_files(),
        _get_third_root(),
        _get_third_empty(),
        *_get_third_files(),
    ]

    def individual_test(root_path: Path) -> None:
        _common_test(expected, walk_iterator(root_path), root_path)

    _inside_temporary_directory(individual_test)


def test_depth() -> None:
    expected: Strs2 = [
        _get_second_empty(),
        *_get_second_files(),
        _get_third_root(),
    ]

    def individual_test(root_path: Path) -> None:
        _common_test(expected, walk_iterator(root_path, depth=2), root_path)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    expected: Strs2 = [
        *_get_first_files(),
        *_get_second_files(),
        *_get_third_files(),
    ]

    def individual_test(root_path: Path) -> None:
        _common_test(
            expected, walk_iterator(root_path, directory=False), root_path
        )

    _inside_temporary_directory(individual_test)


def test_file() -> None:
    expected: Strs2 = [
        _get_first_empty(),
        _get_second_root(),
        _get_second_empty(),
        _get_third_root(),
        _get_third_empty(),
    ]

    def individual_test(root_path: Path) -> None:
        _common_test(expected, walk_iterator(root_path, file=False), root_path)

    _inside_temporary_directory(individual_test)


def test_suffix() -> None:
    expected: Strs2 = [
        _get_first_json(),
        _get_second_json(),
        _get_third_json(),
    ]

    def individual_test(root_path: Path) -> None:
        _common_test(
            expected,
            walk_iterator(root_path, directory=False, suffix="json"),
            root_path,
        )

    _inside_temporary_directory(individual_test)


def test_filter() -> None:
    expected: Strs2 = [_get_third_text()]

    def individual_test(root_path: Path) -> None:
        _common_test(
            expected,
            walk_iterator(root_path, glob_filter="*/*/*.txt"),
            root_path,
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_all()
    test_depth()
    test_directory()
    test_file()
    test_suffix()
    test_filter()
    return True
