#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to remove file or directory and log history."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.bool_context import BoolPair
from pyspartaproj.context.extension.path_context import PathPair2, Paths
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.file.json.convert_from_json import (
    path_pair2_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.status.check_exists import check_exists_pair
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _common_test(history_size: int, history_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(history_path))
    assert history_size == len(history)

    for _, path_pair in history.items():
        exists_pair: BoolPair = check_exists_pair(path_pair)
        assert bool_same_array(
            [not exists_pair["source.path"], exists_pair["destination.path"]]
        )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _finalize_remove(path: Path, safe_trash: SafeTrash) -> Path:
    safe_trash.trash(path)
    return safe_trash.pop_history()


def _finalize_remove_array(paths: Paths, safe_trash: SafeTrash) -> Path:
    safe_trash.trash_at_once(paths)
    return safe_trash.pop_history()


def _finalize_remove_tree(
    paths: Paths, temporary_root: Path, safe_trash: SafeTrash
) -> Path:
    safe_trash.trash_at_once(paths, trash_root=temporary_root)
    return safe_trash.pop_history()


def test_file() -> None:
    """Test to remove file, and log history."""

    def individual_test(temporary_root: Path) -> None:
        safe_trash = SafeTrash()
        _common_test(
            1,
            _finalize_remove(
                create_temporary_file(temporary_root), safe_trash
            ),
        )

    _inside_temporary_directory(individual_test)


def test_exists() -> None:
    """Test to remove same files at twice."""

    def individual_test(temporary_root: Path) -> None:
        source_root: Path = create_temporary_file(temporary_root)
        remove_paths: Paths = [source_root] * 2
        safe_trash = SafeTrash()
        history_path: Path = _finalize_remove_array(remove_paths, safe_trash)
        _common_test(1, history_path)

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to remove files and directories, and log history."""

    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root, tree_deep=3)
        remove_paths: Paths = list(walk_iterator(temporary_root, depth=1))
        safe_trash = SafeTrash()
        history_path: Path = _finalize_remove_tree(
            remove_paths, temporary_root, safe_trash
        )
        _common_test(len(remove_paths), history_path)

    _inside_temporary_directory(individual_test)


def test_select() -> None:
    """Test to remove file, and using specific trash box path."""
    with TemporaryDirectory() as temporary_path:

        def individual_test(temporary_root: Path) -> None:
            source_root: Path = create_temporary_tree(temporary_root)
            remove_paths: Paths = list(walk_iterator(source_root, depth=1))
            safe_trash = SafeTrash(history_path=Path(temporary_path))
            history_path: Path = _finalize_remove_array(
                remove_paths, safe_trash
            )
            _common_test(len(remove_paths), history_path)

        _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_exists()
    test_tree()
    test_select()
    return True
