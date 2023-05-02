#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from scripts.times.current_datetime import get_current_time


def _common_test(time: datetime, expected: str) -> None:
    assert datetime.fromisoformat(expected) == time


def test_utc() -> None:
    EXPECTED: str = '2023-04-01T00:00:00+00:00'
    _common_test(get_current_time(override=True), EXPECTED)


def test_jst() -> None:
    EXPECTED: str = '2023-04-01T09:00:00+09:00'
    _common_test(get_current_time(override=True, jst=True), EXPECTED)


def main() -> bool:
    test_utc()
    test_jst()
    return True
