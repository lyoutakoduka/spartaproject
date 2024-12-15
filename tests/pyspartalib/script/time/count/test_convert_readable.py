#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert time from number to readable string."""

from decimal import Decimal

from pyspartalib.context.default.integer_context import IntPair
from pyspartalib.context.default.string_context import StrPair
from pyspartalib.context.extension.decimal_context import DecPair
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.time.count.convert_readable import readable_time

initialize_decimal()


def _common_test(results: StrPair) -> None:
    for expected, result in results.items():
        assert expected == result


def test_datetime() -> None:
    """Test to convert time from number to readable string."""
    assert "2023y 3m 24d 21h 59m 7s" == readable_time(
        Decimal("63849679147.012345")
    )


def test_day() -> None:
    """Test to convert times that is type integer."""
    second: int = 1
    minute: int = second * 60
    hour: int = minute * 60
    day: int = hour * 24

    test_case: IntPair = {
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

    _common_test(
        {
            expected: readable_time(Decimal(str(source)))
            for expected, source in test_case.items()
        }
    )


def test_second() -> None:
    """Test to convert times including decimal point."""
    test_case: DecPair = dict(
        zip(
            [
                "1.000000s",
                "0.100000s",
                "0.010000s",
                "0.001000s",
                "0.000100s",
                "0.000010s",
                "0.000001s",
                "0.000000s",
            ],
            [Decimal("0.1") ** Decimal(str(i)) for i in range(9)],
        )
    )

    _common_test(
        {
            expected: readable_time(source, digit=6)
            for expected, source in test_case.items()
        }
    )


def test_digit() -> None:
    """Test to convert times including decimal point by specific digit."""
    test_case: IntPair = {
        "0s": 0,
        "0.6s": 1,
        "0.66s": 2,
        "0.666s": 3,
        "0.6666s": 4,
        "0.66666s": 5,
        "0.666666s": 6,
    }

    _common_test(
        {
            expected: readable_time(Decimal("0.6666666"), digit=source)
            for expected, source in test_case.items()
        }
    )
