#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to count time like a timer."""

from datetime import datetime, timezone
from decimal import Decimal

from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.time.stamp.get_time_stamp import get_initial_epoch

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
            self._count = get_initial_epoch()
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
                The argument is mainly used for test.

            interval (Decimal | None, optional): Defaults to None.
                Interval of timer count, use 1 if None.
                The argument is mainly used for test.

        Use this class as like follow script,
            if you want to get current date time represented by epoch time.

        >>> import time
        >>> timer = TimerSelect() # Create class instance.
        >>> timer() # Use __call___ method, and get current date time.
        1704010500
        >>> time.sleep(1)
        >>> timer()
        1704010501

        If in the test environment.

        >>> timer = TimerSelect(override=True, interval=Decimal("0.1"))
        >>> timer()
        1680307200
        >>> timer.increase_timer() # Increase timer count by 0.1.
        >>> timer()
        1680307200.1
        """
        if interval is None:
            interval = Decimal("1")

        self._initialize_variable(override, interval)
        self._initialize_current()
