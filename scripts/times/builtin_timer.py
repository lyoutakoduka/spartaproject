#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import timezone, datetime

from scripts.decimal_context import set_decimal_context

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

    def __init__(self, override: bool = False, interval: Decimal = Decimal('1')) -> None:
        self._override: bool = override
        self._interval: Decimal = interval

        self._initialize_current()

    def current(self) -> Decimal:
        return self._count

    def __call__(self) -> Decimal:
        if self._override:
            self._count += self._interval
        else:
            self._count = self._get_current()

        return self.current()
