#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import modf
from datetime import datetime, timedelta
from typing import List, TypedDict

_Strs = List[str]


class _Formatter(TypedDict):
    id: str
    count: float


_Formatters = List[_Formatter]


def _add_without_float_error(second: float, micro_sec: float) -> float:
    micro_scale: float = 1.0e+6
    second_int: int = int(second * micro_scale + micro_sec)

    return second_int / micro_scale


def _merge_second(counter: datetime) -> float:
    second: float = counter.second
    micro_sec: float = counter.microsecond

    if 0 == micro_sec:
        return second

    return _add_without_float_error(second, micro_sec)


def _get_format(counter: datetime) -> _Formatters:
    return [
        {'id': 'year', 'count': counter.year - 1},
        {'id': 'month', 'count': counter.month - 1},
        {'id': 'day', 'count': counter.day - 1},
        {'id': 'hour', 'count': counter.hour},
        {'id': 'minute', 'count': counter.minute},
        {'id': 'second', 'count': _merge_second(counter)},
    ]


def _format_second_float(count_float: float, order: int, order_limit: int) -> float:
    count_float = count_float * pow(10, order)
    count_float = round(count_float)
    return count_float * pow(10, order_limit - order)


def _format_second_str(count_text: str, order: int, order_limit: int) -> str:
    count_text = count_text.zfill(order_limit)
    return count_text[:order]


def _format_second_text(count_float: float, order: int) -> str:
    ORDER_LIMIT: int = 6

    if ORDER_LIMIT < order:
        order = ORDER_LIMIT

    count_float = _format_second_float(count_float, order, ORDER_LIMIT)
    return _format_second_str(str(count_float), order, ORDER_LIMIT)


def _get_second_text(count: float, order: int) -> str:
    if 0 == order:
        return str(round(count))

    count_float, count_int = modf(count)
    clipped_numbers = [
        str(int(count_int)),
        _format_second_text(count_float, order)
    ]

    return '.'.join(clipped_numbers)


def _get_count_texts(formatters: _Formatters, order: int) -> _Strs:
    count_texts: _Strs = []

    for formatter in formatters:
        id: str = formatter['id']
        count: float = formatter['count']
        count_text: str = str(count)

        if 'second' == id:
            count_text = _get_second_text(count, order)
        else:
            if count == 0:
                continue

        count_texts += [count_text + id[0]]

    return count_texts


def readable_time(second: float, order: int = 0) -> str:
    formatters: _Formatters = _get_format(
        datetime.min + timedelta(seconds=second))

    return ' '.join(_get_count_texts(formatters, order))
