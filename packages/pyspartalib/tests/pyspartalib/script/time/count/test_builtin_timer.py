#!/usr/bin/env python

"""Test module to count time like a timer."""

from decimal import Decimal
from time import sleep

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.decimal_context import Decs
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.time.count.builtin_timer import TimerSelect
from pyspartalib.script.time.epoch.get_time_stamp import get_initial_epoch

initialize_decimal()


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_interval() -> Decimal:
    return Decimal("0.005")


def _get_starting_point(timer: TimerSelect) -> Decimal:
    return timer()


def _sleep_interval() -> None:
    sleep(float(_get_interval()))


def _get_elapsed_time(timer: TimerSelect, begin: Decimal) -> Decimal:
    return timer() - begin


def _get_time_array() -> Decs:
    return [Decimal(str(i)) for i in range(10)]


def _get_timer_results(timer: TimerSelect) -> Decs:
    results: Decs = []

    for _ in range(10):
        results += [timer()]
        timer.increase_timer()

    return results


def _check_counter_result(expected: Decs, timer: TimerSelect) -> None:
    results: Decs = _get_timer_results(timer)

    _difference_error(
        [count + get_initial_epoch() for count in expected],
        results,
    )


def test_builtin() -> None:
    """Test to count timer."""
    timer = TimerSelect()
    begin: Decimal = _get_starting_point(timer)

    _sleep_interval()

    _fail_error(_get_interval() < _get_elapsed_time(timer, begin))


def test_integer() -> None:
    """Test to count timer with test mode."""
    _check_counter_result(_get_time_array(), TimerSelect(override=True))


def test_interval() -> None:
    """Test to count timer with test mode by specific interval."""
    micro_scale: Decimal = Decimal("0.000001")

    _check_counter_result(
        [expected * micro_scale for expected in _get_time_array()],
        TimerSelect(override=True, interval=micro_scale),
    )
