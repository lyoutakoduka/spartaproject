#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get latest date time of file or directory as time object."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import StrPair
from pyspartaproj.context.extension.time_context import TimePair, Times
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.bool.compare_json import is_same_json
from pyspartaproj.script.directory.create_directory import create_directory
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


def _get_latest_pair(path: Path, jst: bool) -> Times:
    return [
        get_latest(path, access=status, jst=jst) for status in [False, True]
    ]


def _compare_utc_timezone(path: Path) -> None:
    _common_test(_get_latest_pair(path, False))


def _compare_jst_timezone(path: Path) -> Times:
    times: Times = _get_latest_pair(path, True)
    _common_test(times)

    return times


def _convert_time_to_text(times: TimePair) -> StrPair:
    return {path_text: time.isoformat() for path_text, time in times.items()}


def _get_json_latest(file_path: Path, status: bool) -> Json:
    return multiple_to_json(
        _convert_time_to_text(
            get_directory_latest(walk_iterator(file_path), access=status)
        )
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to get latest date time of file with readable format."""

    def individual_test(temporary_root: Path) -> None:
        _compare_utc_timezone(create_temporary_file(temporary_root))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to get latest date time of directory with readable format."""

    def individual_test(temporary_root: Path) -> None:
        _compare_utc_timezone(
            create_directory(Path(temporary_root, "temporary"))
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    """Test to get latest date time of file as JST time zone."""

    def individual_test(temporary_root: Path) -> None:
        times: Times = _compare_jst_timezone(
            create_temporary_file(temporary_root)
        )

        assert "9:00:00" == str(times[0].utcoffset())

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to get latest date time of contents in the directory you select."""

    def individual_test(temporary_root: Path) -> None:
        file_path: Path = create_temporary_tree(Path(temporary_root, "tree"))

        assert is_same_json(
            *[_get_json_latest(file_path, status) for status in [False, True]]
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_directory()
    test_jst()
    test_tree()
    return True
