#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from typing import List
from decimal import Decimal

from scripts.decimal_context import set_decimal_context
from scripts.times.builtin_timer import TimerSelect

_Decimals = List[Decimal]


set_decimal_context()

COUNT: int = 10
INI_EXPECTED: _Decimals = [Decimal(str(i)) for i in range(COUNT)]


def _check_counter_result(expected: _Decimals, timer: TimerSelect) -> None:
    expected = [count + timer.APRIL_1_2023_EPOCH for count in expected]

    results: _Decimals = []
    for _ in range(COUNT):
        results += [timer()]
        timer.increase_timer()

    assert expected == results


def test_int() -> None:
    _check_counter_result(INI_EXPECTED, TimerSelect(override=True))


def test_interval() -> None:
    micro_scale: Decimal = Decimal('0.000001')

    _check_counter_result(
        [expected * micro_scale for expected in INI_EXPECTED],
        TimerSelect(override=True, interval=micro_scale)
    )


def test_builtin() -> None:
    timer = TimerSelect()
    interval: Decimal = Decimal('0.005')
    begin: Decimal = timer()
    sleep(float(interval))
    compute_error: Decimal = timer() - begin
    assert Decimal('0.007') > compute_error


def main() -> bool:
    test_int()
    test_interval()
    test_builtin()
    return True
