#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spartaproject.context.default.string_context import Strs
from spartaproject.context.extension.decimal_context import (
    Decimal, set_decimal_context)
from spartaproject.script.time.convert_readable import readable_time
from spartaproject.script.time.count.builtin_timer import TimerSelect

set_decimal_context()


class LogTimer:
    def __init__(self) -> None:
        self.restart()

    def _timer_current(self) -> Decimal:
        return self._timer()

    def increase_timer(self) -> None:
        self._timer.increase_timer()

    def restart(
        self,
        override: bool = False,
        timer_interval: Decimal = Decimal('0.01'),
        interval: Decimal = Decimal('0.1'),
        order: int = 1
    ):
        self._timer: TimerSelect = TimerSelect(
            override=override, interval=timer_interval
        )
        self._start_time: Decimal = self._timer_current()

        self._old_time: int = 0
        self._interval: Decimal = interval

        self._order: int = order

    def _is_force_show(self, elapsed: Decimal) -> bool:
        current_interval: int = int(elapsed / self._interval)
        count_changed: bool = current_interval != self._old_time
        self._old_time = current_interval

        return count_changed

    def show(
        self, force: bool = False, header: Strs = [], footer: Strs = []
    ) -> None:
        elapsed: Decimal = self._timer_current() - self._start_time

        if force or self._is_force_show(elapsed):
            elapsed_text: str = readable_time(elapsed, order=self._order)
            print(' '.join(header + [elapsed_text] + footer))
