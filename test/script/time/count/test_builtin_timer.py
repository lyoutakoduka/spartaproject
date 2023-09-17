#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

from context.extension.decimal_context import (Decimal, Decs,
                                               set_decimal_context)
from script.time.count.builtin_timer import TimerSelect

set_decimal_context()

_COUNT: int = 10
_INI_EXPECTED: Decs = [Decimal(str(i)) for i in range(_COUNT)]


def _check_counter_result(expected: Decs, timer: TimerSelect) -> None:
    expected = [count + timer.APRIL_1_2023_EPOCH for count in expected]

    results: Decs = []
    for _ in range(_COUNT):
        results += [timer()]
        timer.increase_timer()

    assert expected == results


def test_integer() -> None:
    _check_counter_result(_INI_EXPECTED, TimerSelect(override=True))


def test_interval() -> None:
    micro_scale: Decimal = Decimal('0.000001')

    _check_counter_result(
        [expected * micro_scale for expected in _INI_EXPECTED],
        TimerSelect(override=True, interval=micro_scale)
    )


def test_builtin() -> None:
    timer = TimerSelect()
    interval: Decimal = Decimal('0.005')
    begin: Decimal = timer()
    sleep(float(interval))
    compute_error: Decimal = timer() - begin
    assert Decimal('0.015') > compute_error


def main() -> bool:
    test_integer()
    test_interval()
    test_builtin()
    return True
