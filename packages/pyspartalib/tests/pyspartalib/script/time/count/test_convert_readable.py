#!/usr/bin/env python

"""Test module to convert time from number to readable string."""

from decimal import Decimal

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.integer_context import IntPair
from pyspartalib.context.default.string_context import StrPair, Strs
from pyspartalib.context.extension.decimal_context import DecPair, Decs
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.time.count.convert_readable import readable_time

initialize_decimal()


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _common_test(results: StrPair) -> None:
    for expected, result in results.items():
        _difference_error(result, expected)


def test_datetime() -> None:
    """Test to convert time from number to readable string."""
    _difference_error(
        readable_time(Decimal("63849679147.012345")),
        "2023y 3m 24d 21h 59m 7s",
    )


def _get_case_day() -> IntPair:
    second: int = 1
    minute: int = second * 60
    hour: int = minute * 60
    day: int = hour * 24

    return {
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


def _times_key_second() -> Strs:
    return [
        "1.000000s",
        "0.100000s",
        "0.010000s",
        "0.001000s",
        "0.000100s",
        "0.000010s",
        "0.000001s",
        "0.000000s",
    ]


def _times_value_second() -> Decs:
    return [Decimal("0.1") ** Decimal(str(i)) for i in range(9)]


def _get_case_second() -> DecPair:
    return dict(zip(_times_key_second(), _times_value_second(), strict=True))


def _get_case_digit() -> IntPair:
    return {
        "0s": 0,
        "0.6s": 1,
        "0.66s": 2,
        "0.666s": 3,
        "0.6666s": 4,
        "0.66666s": 5,
        "0.666666s": 6,
    }


def test_day() -> None:
    """Test to convert times that is type integer."""
    _common_test(
        {
            expected: readable_time(Decimal(str(source)))
            for expected, source in _get_case_day().items()
        },
    )


def test_second() -> None:
    """Test to convert times including decimal point."""
    _common_test(
        {
            expected: readable_time(source, digit=6)
            for expected, source in _get_case_second().items()
        },
    )


def test_digit() -> None:
    """Test to convert times including decimal point by specific digit."""
    _common_test(
        {
            expected: readable_time(Decimal("0.6666666"), digit=source)
            for expected, source in _get_case_digit().items()
        },
    )
