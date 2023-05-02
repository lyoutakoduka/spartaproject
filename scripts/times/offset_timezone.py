#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


def offset_time(time: datetime) -> datetime:
    offset: timedelta | None = time.utcoffset()

    if offset is None:
        raise TypeError

    time_offset: datetime = time - offset
    return time_offset.replace(tzinfo=timezone.utc)
