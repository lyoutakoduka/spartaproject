#!/usr/bin/env python
# -*- coding: utf-8 -*-


from decimal import Decimal

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.time.convert_readable import readable_time
from pyspartaproj.script.time.count.builtin_timer import TimerSelect

initialize_decimal()


class LogTimer:
    def _timer_current(self) -> Decimal:
        return self._timer()

    def _is_force_show(self, elapsed: Decimal) -> bool:
        current_interval: int = int(elapsed / self._interval)
        count_changed: bool = current_interval != self._old_time
        self._old_time = current_interval

        return count_changed

    def increase_timer(self) -> None:
        self._timer.increase_timer()

    def restart(
        self,
        override: bool = False,
        timer_interval: Decimal | None = None,
        interval: Decimal | None = None,
        digit: int = 1,
    ) -> None:
        if timer_interval is None:
            timer_interval = Decimal("0.01")

        if interval is None:
            interval = Decimal("0.1")

        self._timer: TimerSelect = TimerSelect(
            override=override, interval=timer_interval
        )
        self._start_time: Decimal = self._timer_current()

        self._old_time: int = 0
        self._interval: Decimal = interval

        self._digit: int = digit

    def show(
        self,
        force: bool = False,
        header: Strs | None = None,
        footer: Strs | None = None,
    ) -> None:
        if header is None:
            header = []

        if footer is None:
            footer = []

        elapsed: Decimal = self._timer_current() - self._start_time

        if force or self._is_force_show(elapsed):
            elapsed_text: str = readable_time(elapsed, digit=self._digit)
            print(" ".join(header + [elapsed_text] + footer))

    def __init__(self) -> None:
        self.restart()
