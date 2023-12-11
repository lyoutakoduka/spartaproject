#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.time_context import Times
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.bool.compare_json import is_same_json
from pyspartaproj.script.file.json.convert_to_json import multiple_to_json
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.stamp.get_timestamp import (
    get_directory_latest,
    get_latest,
)


def _common_test(times: Times) -> None:
    assert times[0] == times[1]


def _get_json_latest(file_path: Path, status: bool) -> Json:
    return multiple_to_json(
        get_directory_latest(walk_iterator(file_path), access=status)
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        file_path: Path = create_temporary_file(path)
        _common_test(
            [get_latest(file_path, access=status) for status in [False, True]]
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    def individual_test(path: Path) -> None:
        file_path: Path = create_temporary_file(path)
        times: Times = [
            get_latest(file_path, access=status, jst=True)
            for status in [False, True]
        ]
        _common_test(times)

        assert "9:00:00" == str(times[0].utcoffset())

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(path: Path) -> None:
        file_path: Path = create_temporary_tree(Path(path, "tree"))

        assert is_same_json(
            *[_get_json_latest(file_path, status) for status in [False, True]]
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    test_tree()
    return True
