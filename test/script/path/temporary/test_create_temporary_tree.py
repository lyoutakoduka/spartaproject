#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary files and directories tree."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs, Strs2
from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative_array
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _get_tree_contents(temporary_root: Path) -> Paths:
    return get_relative_array(
        list(walk_iterator(temporary_root)), root_path=temporary_root
    )


def _sort_test(expected: Paths, result: Paths) -> None:
    assert 1 == len(
        set([str(sorted(contents)) for contents in [expected, result]])
    )


def _common_test(temporary_root: Path) -> None:
    assert 0 == len(_get_tree_contents(temporary_root))


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_three_hierarchy() -> Strs2:
    name_dir_1: str = "dir001"
    name_dir_2: str = "dir002"
    name_dirs: Strs = [name_dir_1, name_dir_2]
    name_dir_empty: str = "empty"

    name_ini: str = "file.ini"
    name_json: str = "file.json"
    name_text: str = "file.txt"

    return [
        [name_dir_1],
        [name_dir_empty],
        [name_ini],
        [name_json],
        [name_text],
        name_dirs,
        [name_dir_1, name_dir_empty],
        [name_dir_1, name_ini],
        [name_dir_1, name_json],
        [name_dir_1, name_text],
        name_dirs + [name_dir_empty],
        name_dirs + [name_ini],
        name_dirs + [name_json],
        name_dirs + [name_text],
    ]


def test_three() -> None:
    """Test for contents of the temporary tree which is three hierarchy."""
    expected: Paths = [
        Path(*path_names) for path_names in _get_three_hierarchy()
    ]

    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root, tree_deep=3)
        _sort_test(expected, _get_tree_contents(temporary_root))

    _inside_temporary_directory(individual_test)


def test_deep() -> None:
    """Test for count of hierarchy of the temporary tree."""
    outrange_indices: Ints = [-1, 0, 11, 12, 13]

    def individual_test(temporary_root: Path) -> None:
        for index in outrange_indices:
            create_temporary_tree(temporary_root, tree_deep=index)

        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_weight() -> None:
    """Test for scale of file size which is placed on the temporary tree."""
    outrange_indices: Ints = [-2, -1, 0, 11, 12, 13]

    def individual_test(temporary_root: Path) -> None:
        for index in outrange_indices:
            create_temporary_tree(temporary_root, tree_weight=index)

        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_three()
    test_deep()
    test_weight()
    return True
