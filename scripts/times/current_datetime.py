#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from scripts.times.from_timestamp import time_from_timestamp
from scripts.times.builtin_timer import TimerSelect


def get_current_time(override: bool = False, jst: bool = False) -> datetime:
    timer = TimerSelect(override=override)
    return time_from_timestamp(timer())
