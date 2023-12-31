#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.string.format_texts import format_indent
from pyspartaproj.script.time.count.count_elapsed import LogTimer

initialize_decimal()


def _stdout_check(
    expected: str,
    count: int,
    restart: Callable[[LogTimer], None],
    show: Callable[[LogTimer, int], str | None],
) -> None:
    timer = LogTimer()
    restart(timer)

    results: Strs = []

    for i in range(count):
        if time_text := show(timer, i):
            results += [time_text]

        timer.increase_timer()

    assert format_indent(expected) == "\n".join(results)


def test_day() -> None:
    expected: str = """
        1h 0s
        2h 0s
        3h 0s
        4h 0s
        5h 0s
        6h 0s
        7h 0s
        8h 0s
        9h 0s
        10h 0s
        11h 0s
        12h 0s
    """

    minutes: int = 60
    hour: int = minutes * 60
    day: int = hour * 12
    increase_count: int = day + 1

    def restart_timer(timer: LogTimer) -> None:
        timer.restart(
            override=True,
            timer_interval=Decimal(str(1)),
            interval=Decimal(str(hour)),
            digit=0,
        )

    def show_timer(timer: LogTimer, _: int) -> str | None:
        return timer.get_readable_time()

    _stdout_check(expected, increase_count, restart_timer, show_timer)


def test_show() -> None:
    expected: str = """
        0.1s
        0.2s
        0.3s
        0.4s
        0.5s
        0.6s
        0.7s
        0.8s
        0.9s
    """

    increase_count: int = 100

    def restart_timer(timer: LogTimer) -> None:
        timer.restart(override=True)

    def show_timer(timer: LogTimer, index: int) -> str | None:
        return timer.get_readable_time()

    _stdout_check(expected, increase_count, restart_timer, show_timer)


def test_force() -> None:
    expected: str = """
        i=0, 0.00s
        i=1, 0.01s
        i=2, 0.02s
        i=3, 0.03s
        i=4, 0.04s
    """

    increase_count: int = 5

    def restart_timer(timer: LogTimer) -> None:
        timer.restart(override=True, digit=2)

    def show_timer(timer: LogTimer, index: int) -> str | None:
        result: str = f"i={index}"

        if time_text := timer.get_readable_time(force=True):
            result += ", " + time_text

        return result

    _stdout_check(expected, increase_count, restart_timer, show_timer)


def main() -> bool:
    test_day()
    test_show()
    test_force()
    return True
