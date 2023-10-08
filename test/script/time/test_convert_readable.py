#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.decimal_context import Decs
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.initialize_decimal import initialize_decimal
from pyspartaproj.script.time.convert_readable import readable_time

initialize_decimal()


def test_datetime() -> None:
    input_utc_epoch: Decimal = Decimal("63849679147.012345")
    expected: str = "2023y 3m 24d 21h 59m 7s"

    assert expected == readable_time(input_utc_epoch)


def test_day() -> None:
    second: int = 1
    minute: int = second * 60
    hour: int = minute * 60
    day: int = hour * 24

    input_times: IntPair = {
        "1s": second,
        "1m 0s": minute,
        "1m 1s": minute + second,
        "1h 0s": hour,
        "1h 1m 0s": hour + minute,
        "1h 1m 1s": hour + minute + second,
        "1d 0s": day,
        "1d 1h 0s": day + hour,
        "1d 1h 1m 0s": day + hour + minute,
        "1d 1h 1m 1s": day + hour + minute + second,
    }

    assert bool_same_array(
        [
            expected == readable_time(Decimal(str(input)))
            for expected, input in input_times.items()
        ]
    )


def test_second() -> None:
    inputs: Decs = [Decimal("0.1") ** Decimal(str(i)) for i in range(9)]

    expected: Strs = [
        "1.000000s",
        "0.100000s",
        "0.010000s",
        "0.001000s",
        "0.000100s",
        "0.000010s",
        "0.000001s",
        "0.000000s",
    ]

    assert bool_same_array(
        [
            expected == readable_time(input, order=6)
            for expected, input in zip(expected, inputs)
        ]
    )


def test_order() -> None:
    input_time: Decimal = Decimal("0.6666666")
    input_orders: IntPair = {
        "0s": 0,
        "0.6s": 1,
        "0.66s": 2,
        "0.666s": 3,
        "0.6666s": 4,
        "0.66666s": 5,
        "0.666666s": 6,
    }

    assert bool_same_array(
        [
            expected == readable_time(input_time, order=order)
            for expected, order in input_orders.items()
        ]
    )


def main() -> bool:
    test_datetime()
    test_day()
    test_second()
    test_order()
    return True
