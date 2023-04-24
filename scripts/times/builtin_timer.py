#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import timezone, datetime

from scripts.decimal_context import set_decimal_context

set_decimal_context()


class TimerSelect:
    def __init__(self, override: bool = False, interval: Decimal = Decimal('1')) -> None:
        self._override: bool = override
        self._interval: Decimal = interval

        self.APRIL_1_2023_EPOCH: Decimal = Decimal('1680307200')
        self._count: Decimal = self.APRIL_1_2023_EPOCH

    def current(self) -> Decimal:
        return self._count

    def __call__(self) -> Decimal:
        if self._override:
            self._count += self._interval
        else:
            current_time = datetime.now(timezone.utc)
            self._count = Decimal(str(current_time.timestamp()))

        return self.current()
