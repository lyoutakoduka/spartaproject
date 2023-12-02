#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to copy file or directory and log history."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.path_context import PathPair2
from pyspartaproj.script.bool.same_value import bool_same_pair
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.file.json.convert_from_json import (
    path_pair2_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.check_exists import check_exists_pair
from pyspartaproj.script.path.safe.safe_copy import SafeCopy
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _common_test(rename_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(rename_path))
    assert 1 == len(history)

    for _, path_pair in history.items():
        assert bool_same_pair(check_exists_pair(path_pair))


def _inside_temporary_directory(
    function: Callable[[SafeCopy, Path], None]
) -> None:
    with TemporaryDirectory() as temporary_path:
        function(SafeCopy(), Path(temporary_path))


def _copy(safe_copy: SafeCopy, path: Path) -> Path:
    safe_copy.copy(path, path.with_stem("destination"))
    return safe_copy.pop_history()


def test_file() -> None:
    """Test to copy file, and log history."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        safe_copy.copy(source_path, source_path.with_stem("destination"))

        _common_test(safe_copy.pop_history())

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    """Test to copy file for the situation that destination is existing."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        destination_path: Path = safe_copy.copy(
            source_path, source_path, override=True
        )

        _common_test(safe_copy.pop_history())
        assert destination_path.name.endswith("_")

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to copy directory, and log history."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        _common_test(
            _copy(
                safe_copy, create_directory(Path(temporary_path, "temporary"))
            )
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to copy files and directories, and log history."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        source_path: Path = Path(temporary_path, "temporary")
        create_temporary_tree(source_path, tree_deep=2)
        _common_test(_copy(safe_copy, source_path))

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
