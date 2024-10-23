#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.script.time.format.create_iso_date import get_iso_time
from pyspartaproj.script.time.stamp.current_datetime import get_current_time


def _get_year() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_source() -> IntPair2:
    return {
        "year": _get_year(),
        "hour": {"hour": 0, "minute": 0, "second": 0},
        "zone": {"hour": 0, "minute": 0},
    }


def _get_source_jst() -> IntPair2:
    return {
        "year": _get_year(),
        "hour": {"hour": 9, "minute": 0, "second": 0},
        "zone": {"hour": 9, "minute": 0},
    }


def _compare_time(time: datetime, expected: IntPair2) -> None:
    assert get_iso_time(expected) == time


def test_utc() -> None:
    _compare_time(get_current_time(override=True), _get_source())


def test_jst() -> None:
    _compare_time(get_current_time(override=True, jst=True), _get_source_jst())
