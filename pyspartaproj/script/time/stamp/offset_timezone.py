#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


def _offset(time: datetime, offset: timedelta) -> datetime:
    time_offset: datetime = time - offset
    return time_offset.replace(tzinfo=timezone.utc)


def _add_zone(time: datetime) -> datetime:
    return datetime.fromisoformat(time.isoformat() + "+00:00")


def offset_time(time: datetime) -> datetime:
    if offset := time.utcoffset():
        return _offset(time, offset)

    return _add_zone(time)
