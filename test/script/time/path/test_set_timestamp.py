#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test module to set latest date time of file or directory by time object."""

from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    IntPair3,
)
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.time_context import Times
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.path.get_timestamp import get_latest
from pyspartaproj.script.time.path.set_timestamp import set_latest


def _is_access(group: str) -> bool:
    return group == "access"


def _get_year() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_utc() -> IntPair:
    return {"hour": 0, "minute": 0}


def _get_jst() -> IntPair:
    return {"hour": 9, "minute": 0}


def _get_source() -> IntPair2:
    return {
        "year": _get_year(),
        "hour": {"hour": 0, "minute": 0, "second": 0, "micro": 1},
        "zone": _get_utc(),
    }


def _get_source_access() -> IntPair2:
    return {
        "year": {"year": 2023, "month": 4, "day": 15},
        "hour": {"hour": 20, "minute": 9, "second": 30, "micro": 936886},
        "zone": _get_utc(),
    }


def _get_source_jst() -> IntPair2:
    return {
        "year": _get_year(),
        "hour": {"hour": 9, "minute": 0, "second": 0, "micro": 1},
        "zone": _get_jst(),
    }


def _get_source_jst_access() -> IntPair2:
    return {
        "year": {"year": 2023, "month": 4, "day": 16},
        "hour": {"hour": 5, "minute": 9, "second": 30, "micro": 936886},
        "zone": _get_jst(),
    }


def _time_utc() -> IntPair3:
    return {"update": _get_source(), "access": _get_source_access()}


def _time_jst() -> IntPair3:
    return {"update": _get_source_jst(), "access": _get_source_jst_access()}


def _select_zone(jst: bool = False) -> IntPair3:
    return _time_jst() if jst else _time_utc()


def _get_time_text(jst: bool = False) -> Strs:
    times: Strs = [
        "2023-04-01T00:00:00.000001+00:00",
        "2023-04-15T20:09:30.936886+00:00",
    ]
    times_jst: Strs = [
        "2023-04-01T09:00:00.000001+09:00",
        "2023-04-16T05:09:30.936886+09:00",
    ]

    return times_jst if jst else times


def _convert_input_time(times: Strs) -> Times:
    return [datetime.fromisoformat(time) for time in times]


def _set_latest_datetime(path: Path, time_texts: Strs) -> None:
    for status, time in zip([False, True], _convert_input_time(time_texts)):
        set_latest(path, time, access=status)


def _get_latest_datetime(path: Path) -> Times:
    return [get_latest(path, access=status) for status in [False, True]]


def _get_expected_datetime() -> Times:
    return _convert_input_time(_get_time_text())


def _common_test(path: Path, time_texts: Strs) -> None:
    _set_latest_datetime(path, time_texts)

    for expected, result in zip(
        _get_expected_datetime(), _get_latest_datetime(path)
    ):
        assert result == expected


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to set latest date time of file."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(create_temporary_file(temporary_root), _get_time_text())

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to set latest date time of directory."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(
            create_directory(Path(temporary_root, "temporary")),
            _get_time_text(),
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    """Test to set latest date time of file by JST time zone."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(
            create_temporary_file(temporary_root), _get_time_text(jst=True)
        )

    _inside_temporary_directory(individual_test)
