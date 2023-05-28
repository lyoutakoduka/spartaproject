#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from contexts.bool_context import BoolPair
from contexts.path_context import Path, PathPair2
from scripts.bools.same_value import bool_same_array
from scripts.files.jsons.convert_from_json import path_pair2_from_json
from scripts.files.jsons.import_json import json_import
from scripts.paths.check_exists import check_exists_pair
from scripts.paths.create_temporary_file import create_temporary_file
from scripts.paths.safes.safe_rename import SafeRename


def _common_test(rename_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(rename_path))
    assert 1 == len(history)

    for _, path_pair in history.items():
        exists_pair: BoolPair = check_exists_pair(path_pair)
        assert bool_same_array([
            not exists_pair['source'], exists_pair['destination'],
        ])


def _inside_temporary_directory(
    function: Callable[[Path], None]
) -> None:
    with TemporaryDirectory() as temporary_path:
        function(create_temporary_file(Path(temporary_path)))


def test_single() -> None:
    def individual_test(source_path: Path) -> None:
        safe_rename = SafeRename()
        safe_rename.rename(source_path, source_path.with_stem('destination'))

        _common_test(safe_rename.pop_history())

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    def individual_test(source_path: Path) -> None:
        safe_rename = SafeRename()
        destination_path: Path = safe_rename.rename(
            source_path, source_path, override=True,
        )

        _common_test(safe_rename.pop_history())
        assert destination_path.name.endswith('_')

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_single()
    test_override()
    return True
