#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from pyspartaproj.script.time.stamp.from_timestamp import time_from_timestamp

_INPUT_UTC: str = '2023-04-15T20:09:30.936886+00:00'
_input_time: datetime = datetime.fromisoformat(_INPUT_UTC)
_timestamp: Decimal = Decimal(str(_input_time.timestamp()))


def test_utc() -> None:
    assert _input_time == time_from_timestamp(_timestamp)


def test_jst() -> None:
    EXPECTED: str = '2023-04-16T05:09:30.936886+09:00'
    expected_time: datetime = datetime.fromisoformat(EXPECTED)
    assert expected_time == time_from_timestamp(_timestamp, jst=True)


def main() -> bool:
    test_utc()
    test_jst()
    return True
