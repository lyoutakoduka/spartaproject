#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from spartaproject.context.default.integer_context import IntPair
from spartaproject.context.default.string_context import Strs
from spartaproject.context.extension.decimal_context import (
    Decimal, set_decimal_context)

set_decimal_context()


def _get_datetime_counts(counter: datetime) -> IntPair:
    counts: IntPair = {
        'year': counter.year, 'month': counter.month, 'day': counter.day
    }

    counts = {id: count - 1 for id, count in counts.items()}

    counts.update({
        'hour': counter.hour,
        'minute': counter.minute,
        'second': counter.second,
        'micro': counter.microsecond
    })

    return counts


def _get_micro_second_text(
    second: Decimal, counts: IntPair, order: int, order_limit: int
) -> str:
    count_text: str = str(counts['micro'])

    if '0' != count_text:
        count_text = str(second).split('.')[-1]

    count_text += '0' * order_limit
    return count_text[:order]


def _get_decimal_count_texts(
    second: Decimal, counts: IntPair, order: int
) -> str:
    second_numbers: Strs = [str(counts['second'])]

    ORDER_LIMIT: int = 6
    if ORDER_LIMIT < order:
        order = ORDER_LIMIT

    if 0 < order:
        second_numbers += [
            _get_micro_second_text(second, counts, order, ORDER_LIMIT)
        ]

    return '.'.join(second_numbers) + 's'


def _get_integer_count_texts(counts: IntPair) -> Strs:
    integer_types: Strs = ['year', 'month', 'day', 'hour', 'minute']
    return [
        str(counts[type]) + type[0]
        for type in integer_types
        if 0 < counts[type]
    ]


def readable_time(second: Decimal, order: int = 0) -> str:
    counts: IntPair = _get_datetime_counts(
        datetime.min + timedelta(seconds=float(second))
    )

    count_texts: Strs = _get_integer_count_texts(counts)
    count_texts += [_get_decimal_count_texts(second, counts, order)]

    return ' '.join(count_texts)
