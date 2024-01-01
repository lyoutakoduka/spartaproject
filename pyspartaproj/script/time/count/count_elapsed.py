#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to count timer and return time by readable format."""

from decimal import Decimal

from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.time.convert_readable import readable_time
from pyspartaproj.script.time.count.builtin_timer import TimerSelect

initialize_decimal()


class LogTimer:
    """Class to count timer and return time by readable format."""

    def _initialize_variables(
        self,
        override: bool,
        timer_interval: Decimal,
        interval: Decimal,
        digit: int,
    ) -> None:
        self._timer: TimerSelect = TimerSelect(
            override=override, interval=timer_interval
        )
        self._start_time: Decimal = self._timer_current()

        self._old_time: int = 0
        self._interval: Decimal = interval

        self._digit: int = digit

    def _timer_current(self) -> Decimal:
        return self._timer()

    def _is_force_show(self, elapsed: Decimal) -> bool:
        current_interval: int = int(elapsed / self._interval)
        count_changed: bool = current_interval != self._old_time
        self._old_time = current_interval

        return count_changed

    def get_readable_time(self, force: bool = False) -> str | None:
        """Get current timer count as readable string format.

        Args:
            force (bool, optional): Defaults to False.
                Timer count is forcibly returned if it's True.

        Returns:
            str | None:
                Timer count is returned one time at every specific interval.
                Return None, if timer count is in interval.
        """
        elapsed: Decimal = self._timer_current() - self._start_time

        if force or self._is_force_show(elapsed):
            return readable_time(elapsed, digit=self._digit)

        return None

    def increase_timer(self) -> None:
        """Increase time count by specific interval."""
        self._timer.increase_timer()

    def restart(
        self,
        override: bool = False,
        timer_interval: Decimal | None = None,
        interval: Decimal | None = None,
        digit: int = 1,
    ) -> None:
        """Restart timer functionality, it's become initial status.

        Args:
            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                Use for argument "override" on class "TimerSelect".

            timer_interval (Decimal | None, optional): Defaults to None.
                Interval of timer count.
                Use for argument "interval" on class "TimerSelect".

            interval (Decimal | None, optional): Defaults to None.
                Interval which is use for showing timer count.

            digit (int, optional): Defaults to 1.
                Digit of decimal point about timer count when showing.

        Use this class as like follow script,
            if you want to get current datetime represented by readable time.

        >>> import time
        >>> timer = LogTimer() # Create class instance.
        >>> timer.get_readable_time() # Because still in default interval.
        None
        >>> time.sleep(1) # Wait 1 second.
        >>> timer.get_readable_time() # Timer count can shown.
        1.0s

        If in the test environment.

        >>> timer = LogTimer()
        >>> timer.restart(override=True)
        >>> timer.increase_timer() # Increase timer count by 0.5.
        >>> timer.get_readable_time() # Because still in default interval.
        None
        >>> timer.increase_timer() # Increase timer count by 0.5.
        >>> timer.get_readable_time() # Timer count can shown.
        1.0s
        """
        if timer_interval is None:
            timer_interval = Decimal("0.5")

        if interval is None:
            interval = Decimal("1")

        self._initialize_variables(override, timer_interval, interval, digit)

    def __init__(self) -> None:
        """Initialize instance by method "restart"."""
        self.restart()
