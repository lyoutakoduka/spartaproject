#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from script.time.count.builtin_timer import TimerSelect
from script.time.stamp.from_timestamp import time_from_timestamp


def get_current_time(override: bool = False, jst: bool = False) -> datetime:
    timer = TimerSelect(override=override)
    return time_from_timestamp(timer(), jst=jst)
