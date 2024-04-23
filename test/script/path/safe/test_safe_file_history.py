#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to record paths which is source and destination pair."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import (
    PathPair2,
    Paths2,
    Paths3,
)
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.path.modify.get_relative import is_relative
from pyspartaproj.script.path.safe.safe_file_history import FileHistory
from pyspartaproj.script.stack_frame import current_frame


def _get_group() -> Strs:
    return [group + ".path" for group in ["source", "destination"]]


def _get_current_file() -> Path:
    return current_frame()["file"]


def _compare_path_count(expected: PathPair2, result: PathPair2) -> None:
    assert 1 == len(set([len(history) for history in [expected, result]]))


def _take_out_path(history: PathPair2) -> Paths2:
    return [
        [value[group] for group in _get_group()] for value in history.values()
    ]


def _take_out_path_pair(expected: PathPair2, result: PathPair2) -> Paths3:
    return [_take_out_path(history) for history in [expected, result]]


def _compare_path_name(expected: PathPair2, result: PathPair2) -> None:
    history_path_pair: Paths3 = _take_out_path_pair(expected, result)
    assert history_path_pair[0] == history_path_pair[1]


def _common_test(expected: PathPair2, result: PathPair2) -> None:
    _compare_path_count(expected, result)
    _compare_path_name(expected, result)


def _compare_history(expected: PathPair2, result: PathPair2 | None) -> None:
    if result is None:
        fail()
    else:
        _common_test(expected, result)


def _compare_relative(temporary_root: Path, file_history: FileHistory) -> None:
    assert is_relative(
        file_history.get_history_path(), root_path=temporary_root
    )


def _add_single_history(
    file_history: FileHistory, expected: PathPair2, name: str
) -> None:
    source_path: Path = _get_current_file().parent.with_name("source.json")
    destination_path: Path = source_path.with_stem(name)

    file_history.add_history(source_path, destination_path)
    expected[name] = {
        group: path
        for group, path in zip(_get_group(), [source_path, destination_path])
    }


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_single() -> None:
    """Test to record single source and destination path pair."""
    file_history = FileHistory()
    expected: PathPair2 = {}

    _add_single_history(file_history, expected, "single")
    _compare_history(expected, file_history.close_history())


def test_array() -> None:
    """Test to record multiple source and destination path pair."""
    file_history = FileHistory()
    expected: PathPair2 = {}

    for i in range(10):
        _add_single_history(file_history, expected, str(i).zfill(4))

    _compare_history(expected, file_history.close_history())


def test_history() -> None:
    """Test for specific directory for exporting paths you recorded."""
    with TemporaryDirectory() as temporary_path:
        temporary_root = Path(temporary_path)
        file_history = FileHistory(history_path=temporary_root)

        expected: PathPair2 = {}
        _add_single_history(file_history, expected, "single")

        result: Path | None = file_history.close_history()

        _compare_history(expected, result)
        assert history_path.is_relative_to(temporary_root)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_single()
    test_array()
    test_history()
    return True
