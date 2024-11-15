#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get list of contents in the directory you select."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs, Strs2
from pyspartaproj.context.extension.path_context import PathGene, Paths
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.current.get_relative import (
    get_relative_array,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _get_first_ini() -> Strs:
    return ["file.ini"]


def _get_first_json() -> Strs:
    return ["file.json"]


def _get_first_text() -> Strs:
    return ["file.txt"]


def _get_first_empty() -> Strs:
    return ["empty"]


def _get_first_files() -> Strs2:
    return [_get_first_ini(), _get_first_json(), _get_first_text()]


def _get_second_root() -> Strs:
    return ["dir001"]


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
    return _get_second_root() + ["dir002"]


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
    expected: Strs2, walk_generator: PathGene, root_path: Path
) -> None:
    assert _sorted_match(
        [Path(*path_names) for path_names in expected],
        get_relative_array(list(walk_generator), root_path=root_path),
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(create_temporary_tree(Path(temporary_path), tree_deep=3))


def test_all() -> None:
    """Test to get contents of specific directory."""
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
    """Test to get contents of specific directory layer."""
    expected: Strs2 = [
        _get_second_empty(),
        *_get_second_files(),
        _get_third_root(),
    ]

    def individual_test(root_path: Path) -> None:
        _common_test(expected, walk_iterator(root_path, depth=2), root_path)

    _inside_temporary_directory(individual_test)


def test_file() -> None:
    """Test to get files of selected directory."""
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


def test_directory() -> None:
    """Test to get directories of selected directory."""
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
    """Test to get files of specific file format."""
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
    """Test to get contents of specific directory by Glob format filter."""
    expected: Strs2 = [_get_third_text()]

    def individual_test(root_path: Path) -> None:
        _common_test(
            expected,
            walk_iterator(root_path, glob_filter="*/*/*.txt"),
            root_path,
        )

    _inside_temporary_directory(individual_test)
