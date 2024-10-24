#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.context.extension.time_context import datetime
from pyspartaproj.script.time.stamp.offset_timezone import offset_time


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


def _common_text(source_time: str) -> None:
    expected_utc: str = "2023-04-15T20:09:30.936886+00:00"
    expected: datetime = datetime.fromisoformat(expected_utc)

    assert expected == offset_time(datetime.fromisoformat(source_time))


def test_timezone() -> None:
    source_jst: str = "2023-04-16T05:09:30.936886+09:00"
    _common_text(source_jst)


def test_lost() -> None:
    source_lost: str = "2023-04-15T20:09:30.936886"
    _common_text(source_lost)
