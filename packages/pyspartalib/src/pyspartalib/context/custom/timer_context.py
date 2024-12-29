#!/usr/bin/env python

"""User defined types using class LogTimer."""

from typing import Callable

from pyspartalib.script.time.count.log_timer import LogTimer

TimerFunc = Callable[[LogTimer], None]
TimerIntStrFunc = Callable[[LogTimer, int], str | None]
