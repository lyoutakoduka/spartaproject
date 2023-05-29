#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.decimal_context import Decimal, Decs, set_decimal_context
from context.default.integer_context import IntPair
from project.sparta.context.default.string_context import Strs
from script.bool.same_value import bool_same_array
from script.time.convert_readable import readable_time

set_decimal_context()


def test_datetime() -> None:
    INPUT_UTC_EPOCH: Decimal = Decimal('63849679147.012345')
    EXPECT: str = "2023y 3m 24d 21h 59m 7s"

    assert EXPECT == readable_time(INPUT_UTC_EPOCH)


def test_day() -> None:
    SECOND: int = 1
    MINUTE: int = SECOND * 60
    HOUR: int = MINUTE * 60
    DAY: int = HOUR * 24

    INPUT_TIMES: IntPair = {
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
        expected == readable_time(Decimal(str(input)))
        for expected, input in INPUT_TIMES.items()
    ])


def test_second() -> None:
    INPUTS: Decs = [Decimal('0.1') ** Decimal(str(i)) for i in range(9)]

    EXPECTED: Strs = [
        "1.000000s",
        "0.100000s",
        "0.010000s",
        "0.001000s",
        "0.000100s",
        "0.000010s",
        "0.000001s",
        "0.000000s",
    ]

    assert bool_same_array([
        expected == readable_time(input, order=6)
        for expected, input in zip(EXPECTED, INPUTS)
    ])


def test_order() -> None:
    INPUT_TIME: Decimal = Decimal('0.6666666')
    INPUT_ORDERS: IntPair = {
        "0s": 0,
        "0.6s": 1,
        "0.66s": 2,
        "0.666s": 3,
        "0.6666s": 4,
        "0.66666s": 5,
        "0.666666s": 6,
    }

    assert bool_same_array([
        expected == readable_time(INPUT_TIME, order=order)
        for expected, order in INPUT_ORDERS.items()
    ])


def main() -> bool:
    test_datetime()
    test_day()
    test_second()
    test_order()
    return True
