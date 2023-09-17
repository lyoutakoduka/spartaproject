#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory

from context.default.bool_context import Bools
from context.extension.path_context import Path, PathPair2, Paths2
from script.bool.same_value import bool_same_array
from script.file.json.convert_from_json import path_pair2_from_json
from script.file.json.import_json import json_import
from script.path.safe.safe_file_history import FileHistory


def _compare_path_count(source: Paths2, destination: PathPair2) -> bool:
    return 1 == len(set([len(history) for history in [source, destination]]))


def _compare_path_name(source: Paths2, destination: PathPair2) -> bool:
    same_paths: Bools = []
    for lefts, (_, rights) in zip(source, sorted(destination.items())):
        for i, type in enumerate(['source', 'destination']):
            same_paths += [lefts[i] == rights[type]]
    return bool_same_array(same_paths)


def _common_test(source: Paths2, rename_path: Path) -> None:
    destination: PathPair2 = path_pair2_from_json(json_import(rename_path))

    assert _compare_path_count(source, destination)
    assert _compare_path_name(source, destination)


def _add_single_history(
    file_history: FileHistory, source_history: Paths2, name: str
) -> None:
    source_path: Path = Path(__file__).parent.with_name('source.json')
    destination_path: Path = source_path.with_stem(name)
    file_history.add_history(source_path, destination_path)
    source_history += [[source_path, destination_path]]


def test_single() -> None:
    file_history = FileHistory()
    source_history: Paths2 = []
    _add_single_history(file_history, source_history, 'destination')

    _common_test(source_history, file_history.pop_history())


def test_array() -> None:
    file_history = FileHistory()
    source_history: Paths2 = []
    for i in range(10):
        _add_single_history(file_history, source_history, str(i).zfill(4))

    _common_test(source_history, file_history.pop_history())


def test_history() -> None:
    with TemporaryDirectory() as temporary_path:
        temporary_root = Path(temporary_path)
        file_history = FileHistory(history_path=temporary_root)
        source_history: Paths2 = []
        _add_single_history(file_history, source_history, 'destination')

        history_path: Path = file_history.pop_history()
        _common_test(source_history, history_path)
        assert history_path.is_relative_to(temporary_root)


def main() -> bool:
    test_single()
    test_array()
    test_history()
    return True
