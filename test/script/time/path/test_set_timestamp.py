#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test module to set latest date time of file or directory by time object."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    IntPair3,
)
from pyspartaproj.context.extension.path_context import PathFunc
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.format.create_iso_date import get_iso_time
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


def _get_input_time(times: IntPair3) -> TimePair:
    return {group: get_iso_time(time) for group, time in times.items()}


def _set_latest_pair(path: Path, times: IntPair3) -> None:
    for group, time in _get_input_time(times).items():
        set_latest(path, time, access=_is_access(group))


def _get_latest_pair(path: Path) -> TimePair:
    return {
        group: get_latest(path, access=_is_access(group))
        for group in ["update", "access"]
    }


def _compare_datetime(path: Path, times: IntPair3) -> None:
    _set_latest_pair(path, times)

    for group, expected in _get_input_time(times).items():
        results: TimePair = _get_latest_pair(path)
        assert expected == results[group]


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to set latest date time of file."""

    def individual_test(temporary_root: Path) -> None:
        _compare_datetime(
            create_temporary_file(temporary_root), _select_zone()
        )

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to set latest date time of directory."""

    def individual_test(temporary_root: Path) -> None:
        _compare_datetime(
            create_directory(Path(temporary_root, "temporary")),
            _select_zone(),
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    """Test to set latest date time of file by JST time zone."""

    def individual_test(temporary_root: Path) -> None:
        _compare_datetime(
            create_temporary_file(temporary_root), _select_zone(jst=True)
        )

    _inside_temporary_directory(individual_test)
