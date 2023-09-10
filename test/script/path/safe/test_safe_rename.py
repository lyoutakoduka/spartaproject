#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from context.default.bool_context import BoolPair
from context.extension.path_context import Path, PathPair2
from script.bool.same_value import bool_same_array
from script.directory.create_directory import create_directory
from script.file.json.convert_from_json import path_pair2_from_json
from script.file.json.import_json import json_import
from script.path.check_exists import check_exists_pair
from script.path.safe.safe_rename import SafeRename
from script.path.temporary.create_temporary_file import create_temporary_file


def _common_test(rename_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(rename_path))
    assert 1 == len(history)

    for _, path_pair in history.items():
        exists_pair: BoolPair = check_exists_pair(path_pair)
        assert bool_same_array([
            not exists_pair['source'], exists_pair['destination']
        ])


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    def individual_test(temporary_path: Path) -> None:
        safe_rename = SafeRename()
        source_path: Path = create_temporary_file(temporary_path)
        safe_rename.rename(source_path, source_path.with_stem('destination'))

        _common_test(safe_rename.pop_history())

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    def individual_test(temporary_path: Path) -> None:
        safe_rename = SafeRename()
        source_path: Path = create_temporary_file(temporary_path)
        destination_path: Path = safe_rename.rename(
            source_path, source_path, override=True
        )

        _common_test(safe_rename.pop_history())
        assert destination_path.name.endswith('_')

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    def individual_test(temporary_path: Path) -> None:
        safe_rename = SafeRename()
        source_path: Path = create_directory(Path(temporary_path, 'temporary'))
        safe_rename.rename(source_path, source_path.with_stem('destination'))

        _common_test(safe_rename.pop_history())

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_override()
    test_directory()
    return True
