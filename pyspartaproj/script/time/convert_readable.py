#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from decimal import Decimal

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.initialize_decimal import initialize_decimal

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
        }
    )

    return counts


def _get_micro_second_text(
    second: Decimal, counts: IntPair, digit: int, digit_limit: int
) -> str:
    count_text: str = str(counts["micro"])

    if "0" != count_text:
        count_text = str(second).split(".")[-1]

    count_text += "0" * digit_limit
    return count_text[:digit]


def _get_decimal_count_texts(
    second: Decimal, counts: IntPair, digit: int
) -> str:
    second_numbers: Strs = [str(counts["second"])]

    digit_limit: int = 6
    if digit_limit < digit:
        digit = digit_limit

    if 0 < digit:
        second_numbers += [
            _get_micro_second_text(second, counts, digit, digit_limit)
        ]

    return ".".join(second_numbers) + "s"


def _get_integer_count_texts(counts: IntPair) -> Strs:
    time_types: Strs = ["year", "month", "day", "hour", "minute"]
    return [
        str(counts[time_type]) + time_type[0]
        for time_type in time_types
        if 0 < counts[time_type]
    ]


def readable_time(second: Decimal, digit: int = 0) -> str:
    counts: IntPair = _get_datetime_counts(
        datetime.min + timedelta(seconds=float(second))
    )

    count_texts: Strs = _get_integer_count_texts(counts)
    count_texts += [_get_decimal_count_texts(second, counts, digit)]

    return " ".join(count_texts)
