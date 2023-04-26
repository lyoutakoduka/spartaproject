#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.bools.same_value import bool_same_array
from scripts.paths.check_exists import path_array_exists
from scripts.paths.evacuate_trash import TrashBox
from scripts.paths.create_tmp_tree import create_tree
from scripts.paths.iterate_directory import walk_iterator

_Bools = List[bool]
_Paths = List[Path]


def _check_result_exits(target_paths: _Paths, evacuated_paths: _Paths) -> None:
    same_bools: _Bools = []

    for i, paths in enumerate([target_paths, evacuated_paths]):
        exists: _Bools = path_array_exists(paths)
        same_bools += [bool_same_array(exists, invert=(0 == i))]

    assert bool_same_array(same_bools)


def _inside_tmp_directory(func: Callable[[_Paths], _Paths]) -> None:
    with TemporaryDirectory() as tmp_path:
        root_path: Path = Path(tmp_path)

        create_tree(root_path)
        target_paths: _Paths = [path for path in walk_iterator(root_path)]
        evacuated_paths: _Paths = func(target_paths)

        _check_result_exits(target_paths, evacuated_paths)


def test_default() -> None:
    def make_tree(evacuate_targets: _Paths) -> _Paths:
        trash_box = TrashBox()
        return trash_box.throw_away(evacuate_targets)

    _inside_tmp_directory(make_tree)


def test_select() -> None:
    def make_tree(evacuate_targets: _Paths) -> _Paths:
        with TemporaryDirectory() as tmp_path:
            trash_box = TrashBox(trash_path=Path(tmp_path))
            return trash_box.throw_away(evacuate_targets)

    _inside_tmp_directory(make_tree)


def main() -> bool:
    test_default()
    test_select()
    return True
