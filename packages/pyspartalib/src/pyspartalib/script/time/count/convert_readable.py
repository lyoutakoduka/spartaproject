#!/usr/bin/env python

"""Module to convert time from number to readable string."""

from datetime import datetime, timedelta
from decimal import Decimal

from pyspartalib.context.default.integer_context import IntPair
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal

initialize_decimal()


def _get_datetime_counts(counter: datetime) -> IntPair:
    counts: IntPair = {
        "year": counter.year,
        "month": counter.month,
        "day": counter.day,
    }

    counts = {key: count - 1 for key, count in counts.items()}

    counts.update(
        {
            "hour": counter.hour,
            "minute": counter.minute,
            "second": counter.second,
            "micro": counter.microsecond,
        },
    )

    return counts


def _get_micro_second_text(
    second: Decimal,
    counts: IntPair,
    digit: int,
    digit_limit: int,
) -> str:
    count_text: str = str(counts["micro"])

    if count_text != "0":
        count_text = str(second).split(".")[-1]

    count_text += "0" * digit_limit
    return count_text[:digit]


def _get_decimal_count_texts(
    second: Decimal,
    counts: IntPair,
    digit: int,
) -> str:
    second_numbers: Strs = [str(counts["second"])]
    digit_limit: int = 6
    digit = min(digit_limit, digit)

    if digit > 0:
        second_numbers += [
            _get_micro_second_text(second, counts, digit, digit_limit),
        ]

    return ".".join(second_numbers) + "s"


def _get_integer_count_texts(counts: IntPair) -> Strs:
    return [
        str(counts[time_type]) + time_type[0]
        for time_type in ["year", "month", "day", "hour", "minute"]
        if counts[time_type] > 0
    ]


def _get_time_elements(second: Decimal, digit: int, counts: IntPair) -> Strs:
    return [
        *_get_integer_count_texts(counts),
        _get_decimal_count_texts(second, counts, digit),
    ]


def readable_time(second: Decimal, digit: int = 0) -> str:
    """Convert time from number to readable string.

    Args:
        second (Decimal): Number you want to convert to readable string.

        digit (int, optional): Defaults to 0.
            Digit of decimal point about time string which is returned.

    Returns:
        str: Time converted to readable string.

    """
    counts: IntPair = _get_datetime_counts(
        datetime.min + timedelta(seconds=float(second)),
    )

    return " ".join(_get_time_elements(second, digit, counts))
