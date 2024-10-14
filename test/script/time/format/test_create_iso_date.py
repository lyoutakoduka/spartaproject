#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal
from zoneinfo import ZoneInfo

from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.script.time.format.create_iso_date import (
    get_iso_epoch,
    get_iso_string,
    get_iso_time,
)


def _get_years() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_hours() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30, "micro": 123}


def _get_second() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30}


def _get_zones() -> IntPair:
    return {"hour": 9, "minute": 0}


def _get_source_all() -> IntPair2:
    return {"year": _get_years(), "hour": _get_hours(), "zone": _get_zones()}


def _get_source_micro() -> IntPair2:
    return {"year": _get_years(), "hour": _get_second(), "zone": _get_zones()}


def _set_expected_time(
    year: IntPair, hour: IntPair, tzinfo: ZoneInfo
) -> datetime:
    return datetime(
        year["year"],
        year["month"],
        year["day"],
        hour["hour"],
        hour["minute"],
        hour["second"],
        hour["micro"],
        tzinfo=tzinfo,
    )


def _get_expected_time(source: IntPair2) -> datetime:
    return _set_expected_time(
        source["year"], source["hour"], ZoneInfo("Asia/Tokyo")
    )


def _get_expected_epoch() -> Decimal:
    return Decimal("1680292290.000123")


def _get_source_zone() -> IntPair2:
    return {"year": _get_years(), "hour": _get_hours()}


def _get_expected_all() -> str:
    return "2023-04-01T04:51:30.000123+09:00"


def _get_expected_micro() -> str:
    return "2023-04-01T04:51:30+09:00"


def _get_expected_zone() -> str:
    return "2023-04-01T04:51:30.000123"


def _compare_string(source: IntPair2, expected: str) -> None:
    assert get_iso_string(source) == expected


def _compare_time(source: IntPair2, expected: datetime) -> None:
    assert get_iso_time(source) == expected


def _compare_epoch(source: IntPair2, expected: Decimal) -> None:
    assert get_iso_epoch(source) == expected


def test_all() -> None:
    _compare_string(_get_source_all(), _get_expected_all())


def test_micro() -> None:
    _compare_string(_get_source_micro(), _get_expected_micro())


def test_zone() -> None:
    _compare_string(_get_source_zone(), _get_expected_zone())


def test_time() -> None:
    source: IntPair2 = _get_source_all()
    _compare_time(source, _get_expected_time(source))
