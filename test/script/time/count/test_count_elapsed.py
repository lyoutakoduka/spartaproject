#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from typing import Callable

from pyspartaproj.context.extension.decimal_context import set_decimal_context
from pyspartaproj.script.off_stdout import StdoutText
from pyspartaproj.script.string.format_texts import format_indent
from pyspartaproj.script.time.count.count_elapsed import LogTimer

set_decimal_context()


def _stdout_check(
    expected: str,
    count: int,
    restart: Callable[[LogTimer], None],
    show: Callable[[LogTimer, int], None],
) -> None:
    timer = LogTimer()
    restart(timer)

    stdout_text = StdoutText()

    @stdout_text.decorator
    def _show_log() -> None:
        for i in range(count):
            show(timer, i)
            timer.increase_timer()

    _show_log()

    assert format_indent(expected, stdout=True) == stdout_text.stdout


def test_day() -> None:
    EXPECTED: str = """
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
            order=0,
        )

    def show_timer(timer: LogTimer, _: int) -> None:
        timer.show()

    _stdout_check(EXPECTED, increase_count, restart_timer, show_timer)


def test_show() -> None:
    EXPECTED: str = """
        i=10 Almost 0.1s have passed...
        i=20 Almost 0.2s have passed...
        i=30 Almost 0.3s have passed...
        i=40 Almost 0.4s have passed...
        i=50 Almost 0.5s have passed...
        i=60 Almost 0.6s have passed...
        i=70 Almost 0.7s have passed...
        i=80 Almost 0.8s have passed...
        i=90 Almost 0.9s have passed...
    """

    increase_count: int = 100

    def restart_timer(timer: LogTimer) -> None:
        timer.restart(override=True)

    def show_timer(timer: LogTimer, index: int) -> None:
        timer.show(
            header=[f"i={index}", "Almost"], footer=["have", "passed..."]
        )

    _stdout_check(EXPECTED, increase_count, restart_timer, show_timer)


def test_force() -> None:
    EXPECTED: str = """
        i=0
        0.00s
        i=1
        0.01s
        i=2
        0.02s
        i=3
        0.03s
        i=4
        0.04s
    """

    increase_count: int = 5

    def restart_timer(timer: LogTimer) -> None:
        timer.restart(override=True, order=2)

    def show_timer(timer: LogTimer, index: int) -> None:
        print(f"i={index}")
        timer.show(force=True)

    _stdout_check(EXPECTED, increase_count, restart_timer, show_timer)


def main() -> bool:
    test_day()
    test_show()
    test_force()
    return True
