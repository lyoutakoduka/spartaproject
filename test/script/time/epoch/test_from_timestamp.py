#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert time data from epoch format to datetime object."""

from datetime import datetime
from decimal import Decimal

from pyspartaproj.script.time.epoch.from_timestamp import time_from_timestamp


def _get_input_time() -> datetime:
    return datetime.fromisoformat("2023-04-15T20:09:30.936886+00:00")


def _get_timestamp() -> Decimal:
    return Decimal(str(_get_input_time().timestamp()))


def test_utc() -> None:
    """Test to convert time data from epoch format to datetime object."""
    assert _get_input_time() == time_from_timestamp(_get_timestamp())


def test_jst() -> None:
    """Test to convert time data to datetime object as JST time zone."""
    expected: str = "2023-04-16T05:09:30.936886+09:00"
    assert datetime.fromisoformat(expected) == time_from_timestamp(
        _get_timestamp(), jst=True
    )
