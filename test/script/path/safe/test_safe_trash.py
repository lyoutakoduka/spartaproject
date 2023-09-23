#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.bool_context import BoolPair
from pyspartaproj.context.extension.path_context import PathPair2, Paths
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.file.json.convert_from_json import \
    path_pair2_from_json
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.check_exists import check_exists_pair
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.temporary.create_temporary_file import \
    create_temporary_file
from pyspartaproj.script.path.temporary.create_temporary_tree import \
    create_temporary_tree


def _common_test(history_size: int, history_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(history_path))
    assert history_size == len(history)

    for _, path_pair in history.items():
        exists_pair: BoolPair = check_exists_pair(path_pair)
        assert bool_same_array([
            not exists_pair['source'], exists_pair['destination']
        ])


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    def individual_test(temporary_root: Path) -> None:
        safe_trash = SafeTrash()
        safe_trash.trash(create_temporary_file(temporary_root))
        _common_test(1, safe_trash.pop_history())

    _inside_temporary_directory(individual_test)


def test_exists() -> None:
    def individual_test(temporary_root: Path) -> None:
        source_root: Path = create_temporary_file(temporary_root)
        safe_trash = SafeTrash()
        for _ in range(2):
            safe_trash.trash(source_root)
        _common_test(1, safe_trash.pop_history())

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root, tree_deep=3)

        safe_trash = SafeTrash()
        paths: Paths = list(walk_iterator(temporary_root, depth=1))
        for path in paths:
            safe_trash.trash(path, trash_root=temporary_root)

        _common_test(len(paths), safe_trash.pop_history())

    _inside_temporary_directory(individual_test)


def test_select() -> None:
    with TemporaryDirectory() as temporary_path:
        def individual_test(temporary_root: Path) -> None:
            create_temporary_tree(temporary_root)

            safe_trash = SafeTrash(history_path=Path(temporary_path))
            paths: Paths = list(walk_iterator(temporary_root, depth=1))
            for path in paths:
                safe_trash.trash(path)

            _common_test(len(paths), safe_trash.pop_history())

        _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_exists()
    test_tree()
    test_select()
    return True
