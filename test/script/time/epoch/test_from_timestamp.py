#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert time data from epoch format to datetime object."""

from datetime import datetime
from decimal import Decimal

from pyspartaproj.context.default.integer_context import IntPair2
from pyspartaproj.script.time.epoch.from_timestamp import time_from_timestamp
from pyspartaproj.script.time.format.create_iso_date import (
    get_iso_epoch,
    get_iso_time,
)


def _get_source() -> IntPair2:
    return {
        "year": {"year": 2023, "month": 4, "day": 15},
        "hour": {"hour": 20, "minute": 9, "second": 30, "micro": 936886},
        "zone": {"hour": 0, "minute": 0},
    }


def _get_source_jst() -> IntPair2:
    return {
        "year": {"year": 2023, "month": 4, "day": 16},
        "hour": {"hour": 5, "minute": 9, "second": 30, "micro": 936886},
        "zone": {"hour": 9, "minute": 0},
    }


def _get_input_time() -> datetime:
    return get_iso_time(_get_source())


def _get_timestamp() -> Decimal:
    return get_iso_epoch(_get_source())


def test_utc() -> None:
    """Test to convert time data from epoch format to datetime object."""
    assert _get_input_time() == time_from_timestamp(_get_timestamp())


def test_jst() -> None:
    """Test to convert time data to datetime object as JST time zone."""
    expected: str = "2023-04-16T05:09:30.936886+09:00"
    assert datetime.fromisoformat(expected) == time_from_timestamp(
        _get_timestamp(), jst=True
    )
