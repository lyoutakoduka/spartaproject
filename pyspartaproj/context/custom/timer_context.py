#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable

from pyspartaproj.script.time.count.log_timer import LogTimer

TimerFunc = Callable[[LogTimer], None]
TimerIntStrFunc = Callable[[LogTimer, int], str | None]
