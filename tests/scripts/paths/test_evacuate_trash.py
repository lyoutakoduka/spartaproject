#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from tempfile import TemporaryDirectory

from contexts.bool_context import Bools
from contexts.path_context import Path, Paths
from scripts.bools.same_value import bool_same_array
from scripts.paths.check_exists import path_array_exists
from scripts.paths.evacuate_trash import TrashBox
from scripts.paths.create_tmp_tree import create_tree
from scripts.paths.iterate_directory import walk_iterator


def _common_test(target_paths: Paths, evacuated_paths: Paths) -> None:
    same_bools: Bools = []

    for i, paths in enumerate([target_paths, evacuated_paths]):
        exists: Bools = path_array_exists(paths)
        same_bools += [bool_same_array(exists, invert=(0 == i))]

    assert bool_same_array(same_bools)


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        func(Path(tmp_path))


def test_default() -> None:
    def individual_test(tmp_root: Path) -> None:
        create_tree(tmp_root)

        trash_box = TrashBox()
        walk_paths: Paths = []
        for path in walk_iterator(tmp_root):
            trash_box.throw_away_trash(path)
            walk_paths += [path]

        _common_test(walk_paths, trash_box.pop_evacuated())

    _inside_tmp_directory(individual_test)


def test_select() -> None:
    with TemporaryDirectory() as tmp_path:
        def individual_test(tmp_root: Path) -> None:
            create_tree(tmp_root)

            trash_box = TrashBox(trash_path=Path(tmp_path))
            walk_paths: Paths = []
            for path in walk_iterator(tmp_root):
                trash_box.throw_away_trash(path)
                walk_paths += [path]

            _common_test(walk_paths, trash_box.pop_evacuated())

        _inside_tmp_directory(individual_test)


def main() -> bool:
    test_default()
    test_select()
    return True
