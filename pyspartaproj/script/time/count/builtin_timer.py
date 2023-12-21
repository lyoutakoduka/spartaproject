#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to count time like a timer."""

from datetime import datetime, timezone
from decimal import Decimal

from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal

initialize_decimal()


class TimerSelect:
    """Class to count time like a timer."""

    def _initialize_variable(self, override: bool, interval: Decimal) -> None:
        self._override: bool = override
        self._interval: Decimal = interval

    def _get_current(self) -> Decimal:
        return Decimal(str(datetime.now(timezone.utc).timestamp()))

    def _initialize_current(self) -> None:
        self._count: Decimal = Decimal("0")

        if self._override:
            self.april_1_2023_epoch: Decimal = Decimal("1680307200")
            self._count = self.april_1_2023_epoch
        else:
            self._count = self._get_current()

    def increase_timer(self) -> None:
        """Increase time count by specific interval."""
        self._count += self._interval

    def __call__(self) -> Decimal:
        """Get current time based on specific initial time count.

        Returns:
            Decimal: Current time of timer.
        """
        if self._override:
            return self._count

        return self._get_current()

    def __init__(
        self, override: bool = False, interval: Decimal | None = None
    ) -> None:
        """Initialize variables and timer count.

        Args:
            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                Default is current datetime, it's mainly used for test.

            interval (Decimal | None, optional): Defaults to None.
                Interval of timer count, use 1 if None.
        """
        if interval is None:
            interval = Decimal("1")

        self._initialize_variable(override, interval)
        self._initialize_current()
