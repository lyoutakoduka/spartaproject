#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to record paths which is source and destination pair."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import (
    PathPair,
    PathPair2,
    Paths2,
    Paths3,
)
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.path.modify.get_relative import is_relative
from pyspartaproj.script.path.safe.safe_file_history import FileHistory
from pyspartaproj.script.stack_frame import current_frame


def _get_date_time_root(jst: bool = False) -> Path:
    time_utc: Path = Path("2023", "04", "01", "00", "00", "00", "000000")
    time_jst: Path = Path("2023", "04", "01", "09", "00", "00", "000000")

    return time_jst if jst else time_utc


def _get_history_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "history")


def _get_group() -> Strs:
    return [group + ".path" for group in ["source", "destination"]]


def _get_current_file() -> Path:
    return current_frame()["file"]


def _check_exists(result: Path) -> None:
    assert result.exists()


def _compare_path_pair(result: Path, expected: Path) -> None:
    _check_exists(result)

    assert result == expected


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


def _compare_added(expected: PathPair2, result: PathPair2 | None) -> None:
    if result is None:
        fail()
    else:
        _common_test(expected, result)


def _compare_root(
    temporary_root: Path, date_time_root: Path, file_history: FileHistory
) -> None:
    _compare_path_pair(
        file_history.get_history_root(), Path(temporary_root, date_time_root)
    )


def _relative_test(path: Path, root: Path) -> None:
    _check_exists(path)

    assert is_relative(path, root_path=root)


def _compare_path_before(file_history: FileHistory) -> None:
    assert file_history.get_history_path() is None


def _compare_path_after(
    temporary_root: Path, file_history: FileHistory
) -> None:
    if history_path := file_history.get_history_path():
        _relative_test(history_path, temporary_root)
    else:
        fail()


def _compare_path(temporary_root: Path, file_history: FileHistory) -> None:
    _compare_path_before(file_history)
    file_history.get_history()
    _compare_path_after(temporary_root, file_history)


def _compare_history(file_history: FileHistory) -> None:
    assert file_history.get_history() is None


def _get_expected(source_path: Path, destination_path: Path) -> PathPair:
    return {
        group: path
        for group, path in zip(_get_group(), [source_path, destination_path])
    }


def _add_history(
    file_history: FileHistory, expected: PathPair2, name: str
) -> None:
    source_path: Path = _get_current_file().parent.with_name("source.json")
    destination_path: Path = source_path.with_stem(name)

    file_history.add_history(source_path, destination_path)
    expected[name] = _get_expected(source_path, destination_path)


def _add_history_single(file_history: FileHistory) -> PathPair2:
    expected: PathPair2 = {}

    _add_history(file_history, expected, "single")

    return expected


def _add_history_array(file_history: FileHistory) -> PathPair2:
    expected: PathPair2 = {}

    for i in range(10):
        _add_history(file_history, expected, str(i).zfill(4))

    return expected


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_work() -> None:
    def individual_test(temporary_root: Path) -> None:
        file_history = FileHistory(working_root=temporary_root, override=True)

        _compare_root(temporary_root, _get_date_time_root(), file_history)

    _inside_temporary_directory(individual_test)


def test_history() -> None:
    def individual_test(temporary_root: Path) -> None:
        history_root: Path = _get_history_root(temporary_root)
        file_history = FileHistory(
            working_root=temporary_root,
            history_root=history_root,
            override=True,
        )

        _compare_root(history_root, _get_date_time_root(), file_history)

    _inside_temporary_directory(individual_test)


def test_get() -> None:
    """Test to get current file operation history."""
    file_history = FileHistory()

    _compare_added(
        _add_history_single(file_history), file_history.get_history()
    )

    _compare_history(file_history)


def test_single() -> None:
    """Test to record single source and destination path pair."""
    file_history = FileHistory()

    _compare_added(
        _add_history_single(file_history), file_history.close_history()
    )


def test_array() -> None:
    """Test to record multiple source and destination path pair."""
    file_history = FileHistory()

    _compare_added(
        _add_history_array(file_history), file_history.close_history()
    )


def test_path() -> None:
    """Test for specific directory for exporting paths you recorded."""

    def individual_test(temporary_root: Path) -> None:
        file_history = FileHistory(working_root=temporary_root)

        _add_history_array(file_history)
        _compare_path(temporary_root, file_history)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_work()
    test_history()
    test_get()
    test_single()
    test_array()
    test_path()
    return True
