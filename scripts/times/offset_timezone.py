#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
from dateutil.tz import gettz


def offset_time(time: datetime) -> datetime:
    offset: timedelta | None = time.utcoffset()

    if offset is None:
        return datetime.fromisoformat(time.isoformat() + '+00:00')

    time_offset: datetime = time - offset
    return time_offset.replace(tzinfo=timezone.utc)
