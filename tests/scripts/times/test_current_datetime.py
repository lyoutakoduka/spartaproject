#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scripts.times.current_datetime import get_current_time


def test_utc() -> None:
    EXPECTED: str = '2023-04-01T00:00:00+00:00'
    assert EXPECTED == get_current_time(override=True)


def test_jst() -> None:
    EXPECTED: str = '2023-04-01T09:00:00+09:00'
    assert EXPECTED == get_current_time(override=True, jst=True)


def main() -> bool:
    test_utc()
    test_jst()
    return True
