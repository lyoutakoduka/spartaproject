#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from decimal import Decimal

from scripts.decimal_context import set_decimal_context

set_decimal_context()


class TimerSelect:
    def __init__(self, override: bool = False, interval: Decimal = Decimal('1')) -> None:
        self._override: bool = override
        self._interval: Decimal = interval
        self._count: Decimal = Decimal('0')

    def __call__(self) -> Decimal:
        if not self._override:
            return Decimal(str(time.time()))

        self._count += self._interval
        return self._count
