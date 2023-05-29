#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from script.file.json.export_json import json_export
from script.path.avoid_duplication import get_avoid_path


def _common_test(source_path: Path, destination_path: Path) -> None:
    assert source_path == destination_path


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path, 'temporary.json'))


def test_exists() -> None:
    def individual_test(source_path: Path) -> None:
        source_path = json_export(source_path, 'test')
        _common_test(
            get_avoid_path(source_path),
            source_path.with_name(source_path.name + '_')
        )

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    def individual_test(source_path: Path) -> None:
        _common_test(get_avoid_path(source_path), source_path)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_exists()
    test_empty()
    return True
