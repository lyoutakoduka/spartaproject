#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from decimal import Decimal

from pyspartaproj.script.initialize_decimal import initialize_decimal

initialize_decimal()


class TimerSelect:
    def _get_current(self) -> Decimal:
        current_time: datetime = datetime.now(timezone.utc)
        return Decimal(str(current_time.timestamp()))

    def _initialize_current(self) -> None:
        self._count: Decimal = Decimal("0")

        if self._override:
            self.april_1_2023_epoch: Decimal = Decimal("1680307200")
            self._count = self.april_1_2023_epoch
        else:
            self._count = self._get_current()

    def __init__(
        self, override: bool = False, interval: Decimal | None = None
    ) -> None:
        if interval is None:
            interval = Decimal("1")

        self._override: bool = override
        self._interval: Decimal = interval

        self._initialize_current()

    def increase_timer(self) -> None:
        self._count += self._interval

    def __call__(self) -> Decimal:
        if self._override:
            return self._count

        return self._get_current()
