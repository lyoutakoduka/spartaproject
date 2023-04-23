#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

from scripts.bools.same_value import bool_same_array
from scripts.times.convert_readable import readable_time

_IntPair = Dict[str, int]
_FloatPair = Dict[str, float]


def test_datetime() -> None:
    INPUT_UTC_EPOCH: float = 63849679147
    EXPECT: str = "2023y 3m 24d 21h 59m 7s"

    assert EXPECT == readable_time(INPUT_UTC_EPOCH)


def test_day() -> None:
    SECOND: float = 1
    MINUTE: float = SECOND * 60
    HOUR: float = MINUTE * 60
    DAY: float = HOUR * 24

    INPUT_TIMES: _FloatPair = {
        "1s": SECOND,
        "1m 0s": MINUTE,
        "1m 1s": MINUTE + SECOND,
        "1h 0s": HOUR,
        "1h 1m 0s": HOUR + MINUTE,
        "1h 1m 1s": HOUR + MINUTE + SECOND,
        "1d 0s": DAY,
        "1d 1h 0s": DAY + HOUR,
        "1d 1h 1m 0s": DAY + HOUR + MINUTE,
        "1d 1h 1m 1s": DAY + HOUR + MINUTE + SECOND,
    }

    assert bool_same_array([
        expect == readable_time(input)
        for expect, input in INPUT_TIMES.items()
    ])


def test_second() -> None:
    INPUT_TIMES: _FloatPair = {
        "1.000000s": 1.0,
        "0.100000s": 0.1,
        "0.010000s": 0.01,
        "0.001000s": 0.001,
        "0.000100s": 0.0001,
        "0.000010s": 0.00001,
        "0.000001s": 0.000001,
        "0.000000s": 0.0000001,
    }

    assert bool_same_array([
        expect == readable_time(input, order=6)
        for expect, input in INPUT_TIMES.items()
    ])


def test_order() -> None:
    INPUT_TIME: float = 0.6666666
    INPUT_ORDERS: _IntPair = {
        "1s": 0,
        "0.7s": 1,
        "0.67s": 2,
        "0.667s": 3,
        "0.6667s": 4,
        "0.66667s": 5,
        "0.666667s": 6,
    }

    assert bool_same_array([
        expect == readable_time(INPUT_TIME, order=order)
        for expect, order in INPUT_ORDERS.items()
    ])


def main() -> bool:
    test_datetime()
    test_day()
    test_second()
    test_order()
    return True
