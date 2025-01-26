#!/usr/bin/env python

"""Test module to copy file or directory and log history."""

from collections.abc import Sized
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathPair2
from pyspartalib.script.bool.same_value import bool_same_pair
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.path.safe.safe_copy import SafeCopy
from pyspartalib.script.path.status.check_exists import check_exists_pair
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)

from .context.copy_context import CopyPathFunc


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _length_error(result: Sized, expected: int) -> None:
    if len(result) != expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _compare_empty(history: PathPair2 | None) -> PathPair2:
    filtered: PathPair2 = _none_error(history)

    _length_error(filtered, 1)

    return filtered


def _common_test(history: PathPair2 | None) -> None:
    for path_pair in _compare_empty(history).values():
        _fail_error(bool_same_pair(check_exists_pair(path_pair)))


def _inside_temporary_directory(function: CopyPathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(SafeCopy(), Path(temporary_path))


def _copy(safe_copy: SafeCopy, path: Path) -> PathPair2 | None:
    safe_copy.copy(path, path.with_stem("destination"))
    return safe_copy.close_history()


def _create_tree(path: Path) -> Path:
    return create_directory(Path(path, "temporary"))


def _create_tree_deep(path: Path) -> Path:
    return create_temporary_tree(Path(path, "temporary"), tree_deep=2)


def _copy_override(safe_copy: SafeCopy, path: Path) -> Path:
    return safe_copy.copy(path, path, override=True)


def test_file() -> None:
    """Test to copy file, and log history."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        safe_copy.copy(source_path, source_path.with_stem("destination"))

        _common_test(safe_copy.close_history())

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    """Test to copy file for the situation that destination is existing."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        destination_path: Path = _copy_override(safe_copy, source_path)

        _common_test(safe_copy.close_history())
        _difference_error(
            destination_path,
            source_path.with_stem(source_path.stem + "_"),
        )

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to copy directory, and log history."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        _common_test(_copy(safe_copy, _create_tree(temporary_path)))

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to copy files and directories, and log history."""

    def individual_test(safe_copy: SafeCopy, temporary_path: Path) -> None:
        _common_test(_copy(safe_copy, _create_tree_deep(temporary_path)))

    _inside_temporary_directory(individual_test)
