#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.tz import gettz

from scripts.times.builtin_timer import TimerSelect


def get_current_time(override: bool = False, jst: bool = False) -> datetime:
    timer = TimerSelect(override=override)
    current_time: datetime = datetime.fromtimestamp(float(timer()))
    return current_time.astimezone(gettz('Asia/Tokyo' if jst else 'UTC'))
