#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get latest date time of file or directory as time object."""

from datetime import datetime
from os import utime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.time_context import TimePair, Times
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.stamp.get_timestamp import (
    get_directory_latest,
    get_invalid_time,
    get_latest,
    is_same_stamp,
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


def _set_invalid_datetime(path: Path) -> Path:
    utime(path, (0, 0))
    return path


def _set_invalid_directory(invalid_root: Path) -> None:
    for path in walk_iterator(invalid_root):
        _set_invalid_datetime(path)


def _get_directory_latest(path: Path, access: bool) -> TimePair:
    return get_directory_latest(walk_iterator(path), access=access)


def _get_relative_text(path_text: str, root_path: Path) -> str:
    return str(get_relative(Path(path_text), root_path=root_path))


def _get_relative_latest(path: Path, access: bool = False) -> TimePair:
    return {
        _get_relative_text(path_text, path): time
        for path_text, time in _get_directory_latest(path, access).items()
    }


def _is_access(group: str) -> bool:
    return "access" == group


def _compare_invalid_times(times: TimePair) -> None:
    invalid_time: datetime = get_invalid_time()

    for time in times.values():
        assert invalid_time == time


def _compare_invalid_files(times: TimePair) -> None:
    expected: Strs = ["file.json", "empty", "file.ini", "file.txt"]
    assert 1 == len(
        set([str(sorted(files)) for files in [expected, list(times.keys())]])
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_invalid() -> None:
    """Test to compare the date time used for invalid data check."""
    assert "0001-01-01T00:00:00" == get_invalid_time().isoformat()


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
        directory_path: Path = create_temporary_tree(
            Path(temporary_root, "tree")
        )
        _set_invalid_directory(directory_path)

        times: TimePair = _get_relative_latest(directory_path)

        _compare_invalid_times(times)
        _compare_invalid_files(times)

    _inside_temporary_directory(individual_test)


def test_same() -> None:
    """Test to compare 2 dictionaries about latest date time you got."""

    def individual_test(temporary_root: Path) -> None:
        file_path: Path = create_temporary_tree(Path(temporary_root, "tree"))

        assert is_same_stamp(
            *[
                get_directory_latest(walk_iterator(file_path), access=status)
                for status in [False, True]
            ]
        )

    _inside_temporary_directory(individual_test)
