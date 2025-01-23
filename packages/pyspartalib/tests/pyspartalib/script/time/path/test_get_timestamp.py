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


def _get_jst_time_zone() -> str:
    return "9:00:00"


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


def _get_directory_latest(path: Path) -> TimePair:
    return get_directory_latest(walk_iterator(path))


def _get_latest_pair(path: Path, jst: bool) -> TimePair:
    return {
        group: time
        for group in ["update", "access"]
        if (time := get_latest(path, jst=jst, access=_is_access(group)))
        is not None
    }


def _compare_timezone(path: Path, jst: bool) -> TimePair:
    times: TimePair = _get_latest_pair(path, jst)

    _difference_error(times["update"], times["access"])

    return times


def _get_time_zone(times: TimePair) -> str:
    return str(_none_error(times["update"].utcoffset()))


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_temporary_directory(path: Path) -> Path:
    return create_directory(Path(path, "temporary"))


def _get_temporary_tree(path: Path) -> Path:
    return create_temporary_tree(Path(path, "tree"))


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
        _compare_timezone(_get_temporary_directory(temporary_root), False)

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    """Test to get latest date time of file as JST time zone."""

    def individual_test(temporary_root: Path) -> None:
        _difference_error(
            _get_time_zone(
                _compare_timezone(create_temporary_file(temporary_root), True),
            ),
            _get_jst_time_zone(),
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to get latest date time of contents in the directory you select."""

    def individual_test(temporary_root: Path) -> None:
        directory_path: Path = _get_temporary_tree(temporary_root)

        _set_invalid_directory(directory_path)
        _length_error(_get_directory_latest(directory_path), 0)

    _inside_temporary_directory(individual_test)
