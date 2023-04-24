#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.tz import gettz

from scripts.times.builtin_timer import TimerSelect


def get_current_time(override: bool = False, jst: bool = False) -> str:
    timer = TimerSelect(override=override)
    current_time: datetime = datetime.fromtimestamp(int(timer.current()))
    current_time = current_time.astimezone(gettz('UTC'))

    if jst:
        current_time = current_time.astimezone(gettz('Asia/Tokyo'))

    return current_time.isoformat()
