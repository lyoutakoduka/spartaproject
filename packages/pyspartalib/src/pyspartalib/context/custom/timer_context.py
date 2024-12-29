#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types using class LogTimer."""

from typing import Callable

from pyspartalib.script.time.count.log_timer import LogTimer

TimerFunc = Callable[[LogTimer], None]
TimerIntStrFunc = Callable[[LogTimer, int], str | None]
