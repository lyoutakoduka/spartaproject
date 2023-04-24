#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


def _offset_time(time_object: datetime) -> datetime:
    offset: timedelta | None = time_object.utcoffset()

    if offset is None:
        raise TypeError

    time_offset: datetime = time_object - offset
    return time_offset.replace(tzinfo=timezone.utc)


def offset_time(time: str) -> str:
    time_object: datetime = datetime.fromisoformat(time)
    time_object = _offset_time(time_object)
    return time_object.isoformat()
