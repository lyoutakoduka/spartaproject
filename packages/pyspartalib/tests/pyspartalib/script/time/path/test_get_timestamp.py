#!/usr/bin/env python

"""Test module to get latest date time of file or directory as time object."""

from collections.abc import Sized
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.integer_context import IntPair2
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.extension.time_context import TimePair
from pyspartalib.context.type_context import Type
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.modify.current.get_relative import get_relative
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartalib.script.time.format.create_iso_date import get_iso_time
from pyspartalib.script.time.path.get_timestamp import (
    get_directory_latest,
    get_invalid_time,
    get_latest,
)
from pyspartalib.script.time.path.set_timestamp import set_invalid


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _length_error(result: Sized, expected: int) -> None:
    if len(result) != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _get_expected_files() -> Strs:
    return ["file.json", "empty", "file.ini", "file.txt"]


def _is_access(group: str) -> bool:
    return group == "access"


def _get_source() -> IntPair2:
    return {
        "year": {"year": 1, "month": 1, "day": 1},
        "hour": {"hour": 0, "minute": 0, "second": 0},
        "zone": {"hour": 0, "minute": 0},
    }


def _set_invalid_directory(invalid_root: Path) -> None:
    for path in walk_iterator(invalid_root):
        set_invalid(path)


def _get_directory_latest(path: Path, access: bool) -> TimePair:
    return get_directory_latest(walk_iterator(path), access=access)


def _get_relative_text(path_text: str, root_path: Path) -> str:
    return str(get_relative(Path(path_text), root_path=root_path))


def _get_relative_latest(path: Path, access: bool = False) -> TimePair:
    return {
        _get_relative_text(path_text, path): time
        for path_text, time in _get_directory_latest(path, access).items()
    }


def _get_latest_pair(path: Path, jst: bool) -> TimePair:
    return {
        group: get_latest(path, jst=jst, access=_is_access(group))
        for group in ["update", "access"]
    }


def _compare_timezone(path: Path, jst: bool) -> TimePair:
    times: TimePair = _get_latest_pair(path, jst)

    _difference_error(times["update"], times["access"])

    return times


def _get_invalid_time() -> datetime:
    return get_invalid_time()  # To avoid a circular reference.


def _compare_invalid_times(times: TimePair) -> None:
    invalid_time: datetime = _get_invalid_time()

    for time in times.values():
        _difference_error(invalid_time, time)


def _get_files(times: TimePair, expected: Strs) -> Strs:
    return [str(sorted(files)) for files in [expected, list(times.keys())]]


def _compare_invalid_files(times: TimePair) -> None:
    _length_error(list(set(_get_files(times, _get_expected_files()))), 1)


def _get_time_zone(times: TimePair) -> str:
    return str(_none_error(times["update"].utcoffset()))


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_invalid() -> None:
    """Test to compare the date time used for invalid data check."""
    _difference_error(get_invalid_time(), get_iso_time(_get_source()))


def test_file() -> None:
    """Test to get latest date time of file with readable format."""

    def individual_test(temporary_root: Path) -> None:
        _compare_timezone(create_temporary_file(temporary_root), False)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to get latest date time of directory with readable format."""

    def individual_test(temporary_root: Path) -> None:
        _compare_timezone(
            create_directory(Path(temporary_root, "temporary")),
            False,
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    """Test to get latest date time of file as JST time zone."""

    def individual_test(temporary_root: Path) -> None:
        _difference_error(
            _get_time_zone(
                _compare_timezone(
                    create_temporary_file(temporary_root),
                    True,
                ),
            ),
            "9:00:00",
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to get latest date time of contents in the directory you select."""

    def individual_test(temporary_root: Path) -> None:
        directory_path: Path = create_temporary_tree(
            Path(temporary_root, "tree"),
        )
        _set_invalid_directory(directory_path)

        times: TimePair = _get_relative_latest(directory_path)

        _compare_invalid_times(times)
        _compare_invalid_files(times)

    _inside_temporary_directory(individual_test)
