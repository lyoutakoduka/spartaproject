#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timezone

from spartaproject.context.extension.decimal_context import (
    Decimal, set_decimal_context)

set_decimal_context()


class TimerSelect:
    def _get_current(self) -> Decimal:
        current_time: datetime = datetime.now(timezone.utc)
        return Decimal(str(current_time.timestamp()))

    def _initialize_current(self) -> None:
        self._count: Decimal = Decimal('0')

        if self._override:
            self.APRIL_1_2023_EPOCH: Decimal = Decimal('1680307200')
            self._count = self.APRIL_1_2023_EPOCH
        else:
            self._count = self._get_current()

    def __init__(
        self, override: bool = False, interval: Decimal = Decimal('1')
    ) -> None:
        self._override: bool = override
        self._interval: Decimal = interval

        self._initialize_current()

    def increase_timer(self) -> None:
        self._count += self._interval

    def __call__(self) -> Decimal:
        if self._override:
            return self._count

        return self._get_current()
