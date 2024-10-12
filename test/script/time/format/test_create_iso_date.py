#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.script.time.format.create_iso_date import create_iso_date


def _get_years() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_hours() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30, "millisecond": 123}


def _get_second() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30}


def _get_zones() -> IntPair:
    return {"hour": 9, "minute": 15}


def _get_source_all() -> IntPair2:
    return {"year": _get_years(), "hour": _get_hours(), "zone": _get_zones()}


def _get_source_millisecond() -> IntPair2:
    return {"year": _get_years(), "hour": _get_second(), "zone": _get_zones()}


def _get_source_zone() -> IntPair2:
    return {"year": _get_years(), "hour": _get_hours()}


def _get_expected_all() -> str:
    return "2023-04-01T04:51:30.000123+09:15"


def _get_expected_millisecond() -> str:
    return "2023-04-01T04:51:30+09:15"


def _get_expected_zone() -> str:
    return "2023-04-01T04:51:30.000123"


def _compare_string(expected: IntPair2, result: str) -> None:
    assert create_iso_date(expected) == result


def test_all() -> None:
    _compare_string(_get_source_all(), _get_expected_all())


def test_millisecond() -> None:
    _compare_string(_get_source_millisecond(), _get_expected_millisecond())


def test_zone() -> None:
    _compare_string(_get_source_zone(), _get_expected_zone())
