#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory
from typing import Callable

from spartaproject.context.extension.path_context import Path, PathPair2
from spartaproject.script.bool.same_value import bool_same_pair
from spartaproject.script.directory.create_directory import create_directory
from spartaproject.script.file.json.convert_from_json import \
    path_pair2_from_json
from spartaproject.script.file.json.import_json import json_import
from spartaproject.script.path.check_exists import check_exists_pair
from spartaproject.script.path.safe.safe_copy import SafeCopy
from spartaproject.script.path.temporary.create_temporary_file import \
    create_temporary_file
from spartaproject.script.path.temporary.create_temporary_tree import \
    create_temporary_tree


def _common_test(rename_path: Path) -> None:
    history: PathPair2 = path_pair2_from_json(json_import(rename_path))
    assert 1 == len(history)

    for _, path_pair in history.items():
        assert bool_same_pair(check_exists_pair(path_pair))


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _copy(path: Path) -> Path:
    safe_copy = SafeCopy()
    safe_copy.copy(path, path.with_stem('destination'))
    return safe_copy.pop_history()


def test_file() -> None:
    def individual_test(temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        safe_copy = SafeCopy()
        safe_copy.copy(source_path, source_path.with_stem('destination'))

        _common_test(safe_copy.pop_history())

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    def individual_test(temporary_path: Path) -> None:
        source_path: Path = create_temporary_file(temporary_path)
        safe_copy = SafeCopy()
        destination_path: Path = safe_copy.copy(
            source_path, source_path, override=True
        )

        _common_test(safe_copy.pop_history())
        assert destination_path.name.endswith('_')

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    def individual_test(temporary_path: Path) -> None:
        _common_test(
            _copy(create_directory(Path(temporary_path, 'temporary')))
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(temporary_path: Path) -> None:
        source_path: Path = Path(temporary_path, 'temporary')
        create_temporary_tree(source_path, tree_deep=2)
        _common_test(_copy(source_path))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_override()
    test_directory()
    test_tree()
    return True
