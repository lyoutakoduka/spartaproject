#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from context.extension.path_context import Path, PathPair2
from script.bool.same_value import bool_same_pair
from script.file.json.convert_from_json import path_pair2_from_json
from script.file.json.import_json import json_import
from script.path.check_exists import check_exists_pair
from script.path.safe.safe_copy import SafeCopy
from script.path.temporary.create_temporary_file import create_temporary_file


def _common_test(rename_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(rename_path))
    assert 1 == len(history)

    for _, path_pair in history.items():
        assert bool_same_pair(check_exists_pair(path_pair))


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(create_temporary_file(Path(temporary_path)))


def test_single() -> None:
    def individual_test(source_path: Path) -> None:
        safe_copy = SafeCopy()
        safe_copy.copy(source_path, source_path.with_stem('destination'))

        _common_test(safe_copy.pop_history())

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    def individual_test(source_path: Path) -> None:
        safe_copy = SafeCopy()
        destination_path: Path = safe_copy.copy(
            source_path, source_path, override=True
        )

        _common_test(safe_copy.pop_history())
        assert destination_path.name.endswith('_')

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_single()
    test_override()
    return True
