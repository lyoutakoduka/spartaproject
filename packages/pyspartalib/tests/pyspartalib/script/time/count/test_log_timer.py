#!/usr/bin/env python

"""Test module to count timer and get timer count by readable format."""

from decimal import Decimal

from pyspartalib.context.custom.callable_context import IntStrFunc
from pyspartalib.context.custom.timer_context import TimerFunc, TimerIntStrFunc
from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.time.count.log_timer import LogTimer

initialize_decimal()


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected_base() -> str:
    return """
        1.0s
        2.0s
        3.0s
        4.0s
        5.0s
        6.0s
        7.0s
        8.0s
        9.0s
        10.0s
    """


def _get_expected_interval() -> str:
    return """
        30m 0.0s
        1h 0.0s
        1h 30m 0.0s
        2h 0.0s
        2h 30m 0.0s
        3h 0.0s
        3h 30m 0.0s
        4h 0.0s
        4h 30m 0.0s
        5h 0.0s
    """


def _get_expected_digit() -> str:
    return """
        30m 0.0s
        1h 0.0s
        1h 30m 0.0s
        2h 0.0s
        2h 30m 0.0s
        3h 0.0s
        3h 30m 0.0s
        4h 0.0s
        4h 30m 0.0s
        5h 0.0s
    """


def _get_expected_force() -> str:
    return """
        i=0, 0.0s
        i=1, 0.1s
        i=2, 0.2s
        i=3, 0.3s
        i=4, 0.4s
        i=5, 0.5s
        i=6, 0.6s
        i=7, 0.7s
        i=8, 0.8s
        i=9, 0.9s
    """


def _get_timer_base() -> LogTimer:
    timer = LogTimer()
    timer.restart(override=True)

    return timer


def _get_timer_interval() -> LogTimer:
    minutes: int = 60

    timer = LogTimer()
    timer.restart(
        override=True,
        timer_interval=Decimal(str(minutes * 10)),
        interval=Decimal(str(minutes * 30)),
    )

    return timer


def _get_timer_digit() -> LogTimer:
    interval: Decimal = Decimal(str(0.01))
    digit: int = 3

    timer = LogTimer()
    timer.restart(
        override=True,
        timer_interval=interval,
        interval=interval,
        digit=digit,
    )

    return timer


def _get_timer_force() -> LogTimer:
    timer = LogTimer()
    timer.restart(
        override=True,
        timer_interval=Decimal(str(0.1)),
        interval=Decimal(str(1.0)),
    )

    return timer


def _get_timer_results(
    count: int,
    show: IntStrFunc,
    timer: LogTimer,
) -> Strs:
    results: Strs = []

    for i in range(count):
        if time_text := show(i):
            results += [time_text]

        timer.increase_timer()

    return results


def _get_time(timer: LogTimer) -> str | None:
    return timer.get_readable_time()


def _get_time_force(index: int, timer: LogTimer) -> str:
    result: str = f"i={index}"

    if time_text := timer.get_readable_time(force=True):
        result += ", " + time_text

    return result


def _outside(timer: LogTimer) -> IntStrFunc:
    def _inside(_: int) -> str | None:
        return _get_time(timer)

    return _inside


def _outside_index(timer: LogTimer) -> IntStrFunc:
    def _inside(index: int) -> str | None:
        return _get_time_force(index, timer)

    return _inside


def _stdout_check(
    expected: str,
    count: int,
    timer: LogTimer,
    show: IntStrFunc,
) -> None:
    _difference_error(
        "\n".join(_get_timer_results(count, show, timer)),
        format_indent(expected),
    )


def test_base() -> None:
    """Test to get timer count by readable format."""
    expected: str = _get_expected_base()
    count: int = 20 + 1
    timer: LogTimer = _get_timer_base()

    _stdout_check(expected, count, timer, _outside(timer))


def test_interval() -> None:
    """Test to get timer count with specific interval."""
    expected: str = _get_expected_interval()
    count: int = 30 + 1
    timer: LogTimer = _get_timer_interval()

    _stdout_check(expected, count, timer, _outside(timer))


def test_digit() -> None:
    """Test to get timer count with digit of decimal point."""
    expected: str = _get_expected_digit()
    count: int = 10 + 1
    timer: LogTimer = _get_timer_digit()

    _stdout_check(expected, count, timer, _outside(timer))


def test_force() -> None:
    """Test to get timer count forcibly."""
    expected: str = _get_expected_force()
    count: int = 10
    timer: LogTimer = _get_timer_force()

    _stdout_check(expected, count, timer, _outside_index(timer))
