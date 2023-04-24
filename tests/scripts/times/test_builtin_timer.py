#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from decimal import Decimal

from scripts.decimal_context import set_decimal_context
from scripts.bools.same_value import bool_same_array
from scripts.times.builtin_timer import TimerSelect

_Bools = List[bool]
_Decimals = List[Decimal]


set_decimal_context()

COUNT: int = 10
INI_EXPECTED: _Decimals = [Decimal(str(i + 1)) for i in range(COUNT)]


def _check_counter_result(expected: _Decimals, time: TimerSelect) -> None:
    assert expected == [time() for _ in range(COUNT)]


def test_int() -> None:
    _check_counter_result(INI_EXPECTED, TimerSelect(override=True))


def test_interval() -> None:
    micro_scale: Decimal = Decimal('0.000001')

    _check_counter_result(
        [expected * micro_scale for expected in INI_EXPECTED],
        TimerSelect(override=True, interval=micro_scale)
    )


def test_current() -> None:
    timer = TimerSelect(override=True)
    same_times: _Bools = []

    for _ in range(COUNT):
        increment_time: Decimal = timer()
        current_time: Decimal = timer.current()
        same_times += [increment_time == current_time]

    assert bool_same_array(same_times)


def main() -> bool:
    test_int()
    test_interval()
    test_current()
    return True
