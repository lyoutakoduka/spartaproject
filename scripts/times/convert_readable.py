#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import datetime, timedelta
from typing import List, Dict

from scripts.contexts.decimal_context import set_decimal_context

_Strs = List[str]
_IntPair = Dict[str, int]

set_decimal_context()


def _get_datetime_counts(counter: datetime) -> _IntPair:
    counts: _IntPair = {
        'year': counter.year,
        'month': counter.month,
        'day': counter.day,
    }

    counts = {id: count - 1 for id, count in counts.items()}

    counts.update({
        'hour': counter.hour,
        'minute':  counter.minute,
        'second': counter.second,
        'micro':  counter.microsecond,
    })

    return counts


def _get_micro_second_text(second: Decimal, counts: _IntPair, order: int, order_limit: int) -> str:
    count_text: str = str(counts['micro'])

    if '0' != count_text:
        count_text = str(second).split('.')[-1]

    count_text += '0' * order_limit
    return count_text[:order]


def _get_decimal_count_texts(second: Decimal, counts: _IntPair, order: int) -> str:
    second_numbers: _Strs = [str(counts['second'])]

    ORDER_LIMIT: int = 6

    if ORDER_LIMIT < order:
        order = ORDER_LIMIT

    if 0 < order:
        second_numbers += [
            _get_micro_second_text(second, counts, order, ORDER_LIMIT)]

    return '.'.join(second_numbers) + 's'


def _get_int_count_texts(counts: _IntPair) -> _Strs:
    int_types: _Strs = ['year', 'month', 'day', 'hour', 'minute']
    return [
        str(counts[type]) + type[0]
        for type in int_types
        if 0 < counts[type]
    ]


def readable_time(second: Decimal, order: int = 0) -> str:
    counts: _IntPair = _get_datetime_counts(
        datetime.min + timedelta(seconds=float(second)))

    count_texts: _Strs = _get_int_count_texts(counts)
    count_texts += [_get_decimal_count_texts(second, counts, order)]

    return ' '.join(count_texts)
