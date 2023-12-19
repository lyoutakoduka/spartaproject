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


def _inside_temporary_directory(function: Callable[[Path], None]) -> Paths:
    with TemporaryDirectory() as temporary_path:
        root_path: Path = Path(temporary_path)
        function(root_path)
        return get_relative_array(
            list(walk_iterator(root_path)), root_path=root_path
        )


def test_three() -> None:
    """Test for contents of the temporary tree which is three hierarchy."""
    name_dir_1: str = "dir001"
    name_dir_2: str = "dir002"
    name_dirs: Strs = [name_dir_1, name_dir_2]
    name_dir_empty: str = "empty"

    name_ini: str = "file.ini"
    name_json: str = "file.json"
    name_text: str = "file.txt"

    expected_source: Strs2 = [
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

    expected: Paths = [Path(*path_names) for path_names in expected_source]

    def individual_test(temporary_path: Path) -> None:
        create_temporary_tree(temporary_path, tree_deep=3)

    assert expected == _inside_temporary_directory(individual_test)


def test_deep() -> None:
    """Test for count of hierarchy of the temporary tree."""
    outrange_indices: Ints = [-1, 0, 11, 12, 13]

    def individual_test(temporary_path: Path) -> None:
        for index in outrange_indices:
            create_temporary_tree(temporary_path, tree_deep=index)

    assert 0 == len(_inside_temporary_directory(individual_test))


def test_weight() -> None:
    """Test for scale of file size which is placed on the temporary tree."""
    outrange_indices: Ints = [-2, -1, 0, 11, 12, 13]

    def individual_test(temporary_path: Path) -> None:
        for index in outrange_indices:
            create_temporary_tree(temporary_path, tree_weight=index)

    assert 0 == len(_inside_temporary_directory(individual_test))


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_three()
    test_deep()
    test_weight()
    return True
