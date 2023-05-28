#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from contexts.defaults.bool_context import Bools
from contexts.path_context import Path, Paths
from scripts.bools.same_value import bool_same_array
from scripts.paths.check_exists import check_exists_array
from scripts.paths.create_temporary_file import create_temporary_file
from scripts.paths.create_temporary_tree import create_temporary_tree
from scripts.paths.iterate_directory import walk_iterator
from scripts.paths.safes.safe_trash import TrashBox


def _common_test(target_paths: Paths, evacuated_paths: Paths) -> None:
    same_bools: Bools = []

    for i, paths in enumerate([target_paths, evacuated_paths]):
        exists: Bools = check_exists_array(paths)
        same_bools += [bool_same_array(exists, invert=(0 == i))]

    assert bool_same_array(same_bools)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_pass() -> None:
    def individual_test(temporary_root: Path) -> None:
        file_path: Path = create_temporary_file(temporary_root)
        trash_box = TrashBox()
        trash_box.throw_away_trash(file_path)
        _common_test([file_path], trash_box.pop_evacuated())

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root, tree_deep=3)

        trash_box = TrashBox()
        walk_paths: Paths = []
        for path in walk_iterator(temporary_root):
            trash_box.throw_away_trash(path, trash_root=temporary_root)
            walk_paths += [path]

        _common_test(walk_paths, trash_box.pop_evacuated())

    _inside_temporary_directory(individual_test)


def test_select() -> None:
    with TemporaryDirectory() as temporary_path:
        def individual_test(temporary_root: Path) -> None:
            create_temporary_tree(temporary_root)

            trash_box = TrashBox(trash_path=Path(temporary_path))
            walk_paths: Paths = []
            for path in walk_iterator(temporary_root):
                trash_box.throw_away_trash(path)
                walk_paths += [path]

            _common_test(walk_paths, trash_box.pop_evacuated())

        _inside_temporary_directory(individual_test)


def main() -> bool:
    test_pass()
    test_tree()
    test_select()
    return True
