#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to rename file or directory and log history."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.bool_context import BoolPair
from pyspartaproj.context.extension.path_context import PathPair2
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.path.safe.safe_rename import SafeRename
from pyspartaproj.script.path.status.check_exists import check_exists_pair
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _common_test(history: PathPair2 | None) -> None:
    if history is None:
        fail()

    assert 1 == len(history)

    for _, path_pair in history.items():
        exists_pair: BoolPair = check_exists_pair(path_pair)
        assert bool_same_array(
            [not exists_pair["source.path"], exists_pair["destination.path"]]
        )


def _inside_temporary_directory(
    function: Callable[[SafeRename, Path], None]
) -> None:
    with TemporaryDirectory() as temporary_path:
        function(SafeRename(), Path(temporary_path))


def _rename(safe_rename: SafeRename, path: Path) -> PathPair2 | None:
    safe_rename.rename(path, path.with_stem("destination"))
    return safe_rename.close_history()


def test_file() -> None:
    """Test to rename file, and log history."""

    def individual_test(safe_rename: SafeRename, temporary_path: Path) -> None:
        _common_test(
            _rename(safe_rename, create_temporary_file(temporary_path))
        )

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    """Test to rename file for the situation that destination is existing."""

    def individual_test(safe_rename: SafeRename, temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        destination_path: Path = safe_rename.rename(
            source_path, source_path, override=True
        )
        expected: Path = source_path.with_stem(source_path.stem + "_")

        _common_test(safe_rename.close_history())
        assert expected == destination_path

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to rename directory, and log history."""

    def individual_test(safe_rename: SafeRename, temporary_path: Path) -> None:
        _common_test(
            _rename(
                safe_rename,
                create_directory(Path(temporary_path, "temporary")),
            )
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to rename files and directories, and log history."""

    def individual_test(safe_rename: SafeRename, temporary_path: Path) -> None:
        _common_test(
            _rename(
                safe_rename,
                create_temporary_tree(
                    Path(temporary_path, "temporary"), tree_deep=2
                ),
            )
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_override()
    test_directory()
    test_tree()
    return True
