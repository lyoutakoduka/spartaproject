#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from scripts.files.export_json import json_export
from scripts.paths.avoid_duplication import get_avoid_path


def _common_test(src_path: Path, dist_path: Path) -> None:
    assert src_path == dist_path


def _inside_tmp_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        function(Path(tmp_path, 'tmp.json'))


def test_exists() -> None:
    def individual_test(src_path: Path) -> None:
        src_path = json_export(src_path, 'test')
        _common_test(
            get_avoid_path(src_path), src_path.with_name(src_path.name + '_')
        )

    _inside_tmp_directory(individual_test)


def test_empty() -> None:
    def individual_test(src_path: Path) -> None:
        _common_test(get_avoid_path(src_path), src_path)

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_exists()
    test_empty()
    return True
