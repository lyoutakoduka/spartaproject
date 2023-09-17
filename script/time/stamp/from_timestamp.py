#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from dateutil.tz import gettz


def time_from_timestamp(timestamp: Decimal, jst: bool = False) -> datetime:
    date_time: datetime = datetime.fromtimestamp(float(timestamp))
    return date_time.astimezone(gettz('Asia/Tokyo' if jst else 'UTC'))
