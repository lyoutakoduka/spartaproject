#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from pyspartaproj.script.time.count.builtin_timer import TimerSelect
from pyspartaproj.script.time.epoch.from_timestamp import time_from_timestamp


def get_current_time(override: bool = False, jst: bool = False) -> datetime:
    return time_from_timestamp(TimerSelect(override=override)(), jst=jst)
