#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from time import sleep

from pyspartaproj.context.extension.decimal_context import Decs
from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.time.count.builtin_timer import TimerSelect

initialize_decimal()


def _get_time_array() -> Decs:
    return [Decimal(str(i)) for i in range(10)]


def _check_counter_result(expected: Decs, timer: TimerSelect) -> None:
    results: Decs = []

    for _ in range(10):
        results += [timer()]
        timer.increase_timer()

    assert results == [count + timer.april_1_2023_epoch for count in expected]


def test_integer() -> None:
    _check_counter_result(_get_time_array(), TimerSelect(override=True))


def test_interval() -> None:
    micro_scale: Decimal = Decimal("0.000001")

    _check_counter_result(
        [expected * micro_scale for expected in _get_time_array()],
        TimerSelect(override=True, interval=micro_scale),
    )


def test_builtin() -> None:
    timer = TimerSelect()
    begin: Decimal = timer()

    sleep(float(Decimal("0.005")))

    assert Decimal("0.015") > (timer() - begin)


def main() -> bool:
    test_integer()
    test_interval()
    test_builtin()
    return True
