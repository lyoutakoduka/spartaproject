#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get information about current date time."""

from datetime import datetime

from pyspartalib.script.time.count.builtin_timer import TimerSelect
from pyspartalib.script.time.epoch.from_timestamp import time_from_timestamp


def get_current_time(override: bool = False, jst: bool = False) -> datetime:
    """Get information about current date time.

    Args:
        override (bool, optional): Defaults to False.
            Override initial time count to "2023/4/1:12:00:00-00 (AM)".
            It's used for argument "override" of class "TimerSelect".

        jst (bool, optional): Defaults to False.
            If True, you can get datetime object as JST time zone.
            It's used for argument "jst" of function "time_from_timestamp".

    Returns:
        datetime: _description_
    """
    return time_from_timestamp(TimerSelect(override=override)(), jst=jst)
