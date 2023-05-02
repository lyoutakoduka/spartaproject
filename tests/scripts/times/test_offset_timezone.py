#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.time_context import datetime, Times
from scripts.times.offset_timezone import offset_time


def test_timezone() -> None:
    INPUT_UTC: str = '2023-04-15T20:09:30.936886+00:00'
    INPUT_JST: str = '2023-04-16T05:09:30.936886+09:00'

    times: Times = [
        offset_time(datetime.fromisoformat(input))
        for input in [INPUT_UTC, INPUT_JST]
    ]

    assert times[0] == times[1]


def main() -> bool:
    test_timezone()
    return True
