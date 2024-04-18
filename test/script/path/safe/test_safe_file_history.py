#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to record paths which is source and destination pair."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.bool_context import Bools
from pyspartaproj.context.extension.path_context import PathPair2, Paths2
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.file.json.convert_from_json import (
    path_pair2_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.safe.safe_file_history import FileHistory
from pyspartaproj.script.stack_frame import current_frame


def _get_current_file() -> Path:
    return current_frame()["file"]


def _compare_path_count(source: Paths2, destination: PathPair2) -> bool:
    return 1 == len(set([len(history) for history in [source, destination]]))


def _compare_path_name(source: Paths2, destination: PathPair2) -> bool:
    same_paths: Bools = []
    for lefts, (_, rights) in zip(source, sorted(destination.items())):
        for i, path in enumerate(["source.path", "destination.path"]):
            same_paths += [lefts[i] == rights[path]]

    return bool_same_array(same_paths)


def _common_test(source: Paths2, history_path: Path) -> None:
    destination: PathPair2 = path_pair2_from_json(json_import(history_path))

    assert _compare_path_count(source, destination)
    assert _compare_path_name(source, destination)


def _compare_history(source: Paths2, history_path: Path | None) -> None:
    if history_path is None:
        fail()
    else:
        _common_test(source, history_path)


def _add_single_history(
    file_history: FileHistory, source_history: Paths2, name: str
) -> None:
    source_path: Path = _get_current_file().parent.with_name("source.json")
    destination_path: Path = source_path.with_stem(name)

    file_history.add_history(source_path, destination_path)
    source_history += [[source_path, destination_path]]


def test_name() -> None:
    """Test to get name of file which contain the history of file operation."""
    assert "rename.json" == FileHistory().get_history_name()


def test_single() -> None:
    """Test to record single source and destination path pair."""
    file_history = FileHistory()
    source_history: Paths2 = []

    _add_single_history(file_history, source_history, "destination")
    _common_test(source_history, file_history.close_history())


def test_array() -> None:
    """Test to record multiple source and destination path pair."""
    file_history = FileHistory()
    source_history: Paths2 = []
    for i in range(10):
        _add_single_history(file_history, source_history, str(i).zfill(4))

    _common_test(source_history, file_history.close_history())


def test_history() -> None:
    """Test for specific directory for exporting paths you recorded."""
    with TemporaryDirectory() as temporary_path:
        temporary_root = Path(temporary_path)
        file_history = FileHistory(history_path=temporary_root)
        source_history: Paths2 = []
        _add_single_history(file_history, source_history, "destination")

        history_path: Path | None = file_history.close_history()
        _common_test(source_history, history_path)
        assert history_path.is_relative_to(temporary_root)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_name()
    test_single()
    test_array()
    test_history()
    return True
