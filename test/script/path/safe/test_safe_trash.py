#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to remove file or directory and log history."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.bool_context import BoolPair, Bools
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair2, Paths
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.status.check_exists import check_exists_pair
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _get_group() -> Strs:
    return [group + ".path" for group in ["source", "destination"]]


def _compare_size(history_size: int, history: PathPair2 | None) -> PathPair2:
    if history is None:
        fail()

    assert history_size == len(history)

    return history


def _common_test(history_size: int, history: PathPair2 | None) -> None:
    for path_pair in _compare_size(history_size, history).values():
        exists_pair: BoolPair = check_exists_pair(path_pair)
        exists_array: Bools = [exists_pair[group] for group in _get_group()]

        assert bool_same_array([not exists_array[0], exists_array[1]])


def _remove_test(remove_paths: Paths, history: PathPair2 | None) -> None:
    _common_test(len(remove_paths), history)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _finalize_remove(path: Path, safe_trash: SafeTrash) -> PathPair2 | None:
    safe_trash.trash(path)
    return safe_trash.get_history()


def _finalize_remove_array(
    paths: Paths, safe_trash: SafeTrash
) -> PathPair2 | None:
    safe_trash.trash_at_once(paths)
    return safe_trash.get_history()


def _finalize_remove_tree(
    paths: Paths, temporary_root: Path, safe_trash: SafeTrash
) -> PathPair2 | None:
    safe_trash.trash_at_once(paths, trash_root=temporary_root)
    return safe_trash.get_history()


def _get_removal_target(temporary_root: Path) -> Paths:
    return list(walk_iterator(temporary_root, depth=1))


def _get_remove() -> SafeTrash:
    return SafeTrash()


def _get_remove_local(outside_root: Path) -> SafeTrash:
    return SafeTrash(remove_root=outside_root)


def test_file() -> None:
    """Test to remove file, and log history."""

    def individual_test(temporary_root: Path) -> None:
        if safe_trash := _get_remove():
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
        if safe_trash := _get_remove():
            _common_test(
                1,
                _finalize_remove_array(
                    [create_temporary_file(temporary_root)] * 2, safe_trash
                ),
            )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to remove files and directories, and log history."""

    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root, tree_deep=3)
        remove_paths: Paths = _get_removal_target(temporary_root)

        if safe_trash := _get_remove():
            _remove_test(
                remove_paths,
                _finalize_remove_tree(
                    remove_paths, temporary_root, safe_trash
                ),
            )

    _inside_temporary_directory(individual_test)


def test_select() -> None:
    """Test to remove file, and using specific trash box path."""

    def outside_test(outside_root: Path) -> None:
        def individual_test(temporary_root: Path) -> None:
            create_temporary_tree(temporary_root)
            remove_paths: Paths = _get_removal_target(temporary_root)

            _remove_test(
                remove_paths,
                _finalize_remove_array(
                    remove_paths, _get_remove_local(outside_root)
                ),
            )

        _inside_temporary_directory(individual_test)

    _inside_temporary_directory(outside_test)


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
