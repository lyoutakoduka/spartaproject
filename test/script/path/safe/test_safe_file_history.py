#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to record paths which is source and destination pair."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.bool_context import Bools
from pyspartaproj.context.extension.path_context import PathPair2, Paths2
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.path.safe.safe_file_history import FileHistory
from pyspartaproj.script.stack_frame import current_frame


def _get_current_file() -> Path:
    return current_frame()["file"]


def _compare_path_count(expected: PathPair2, result: PathPair2) -> None:
    assert 1 == len(set([len(history) for history in [expected, result]]))


def _compare_path_name(expected: PathPair2, result: PathPair2) -> None:
    same_paths: Bools = []

    for lefts, (_, rights) in zip(expected, sorted(result.items())):
        for i, path in enumerate(["source.path", "destination.path"]):
            same_paths += [lefts[i] == rights[path]]

    assert bool_same_array(same_paths)


def _common_test(expected: PathPair2, result: PathPair2) -> None:
    _compare_path_count(expected, result)
    _compare_path_name(expected, result)


def _compare_history(expected: PathPair2, result: PathPair2 | None) -> None:
    if result is None:
        fail()
    else:
        _common_test(expected, result)


def _add_single_history(
    file_history: FileHistory, expected: PathPair2, name: str
) -> None:
    source_path: Path = _get_current_file().parent.with_name("source.json")
    destination_path: Path = source_path.with_stem(name)

    file_history.add_history(source_path, destination_path)

    expected[name] = {
        "source.path": source_path,
        "destination.path": destination_path,
    }


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
