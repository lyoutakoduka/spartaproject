#!/usr/bin/env python

"""Test module to offset date time by current time zone to UTC time."""

from pyspartalib.context.default.integer_context import IntPair, IntPair2
from pyspartalib.context.extension.time_context import Times
from pyspartalib.context.type_context import Type
from pyspartalib.script.time.format.create_iso_date import get_iso_time
from pyspartalib.script.time.stamp.offset_timezone import offset_time


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_year() -> IntPair:
    return {"year": 2023, "month": 4, "day": 15}


def _get_hour() -> IntPair:
    return {"hour": 20, "minute": 9, "second": 30, "micro": 936886}


def _get_source() -> IntPair2:
    return {
        "year": _get_year(),
        "hour": _get_hour(),
        "zone": {"hour": 0, "minute": 0},
    }


def _get_source_jst() -> IntPair2:
    return {
        "year": {"year": 2023, "month": 4, "day": 16},
        "hour": {"hour": 5, "minute": 9, "second": 30, "micro": 936886},
        "zone": {"hour": 9, "minute": 0},
    }


def _get_source_missing() -> IntPair2:
    return {
        "year": _get_year(),
        "hour": _get_hour(),
    }


def _convert_datetime(time_pairs: IntPair2) -> Times:
    return [
        get_iso_time(time_pair) for time_pair in [_get_source(), time_pairs]
    ]


def _compare_datetime(time_pairs: IntPair2) -> None:
    times: Times = _convert_datetime(time_pairs)

    _difference_error(offset_time(times[1]), times[0])


def test_jst() -> None:
    """Test to compare date time in JST time zone."""
    _compare_datetime(_get_source_jst())


def test_missing() -> None:
    """Test to compare date time that some value is missing."""
    _compare_datetime(_get_source_missing())
