#!/usr/bin/env python

"""Module to offset date time by current time zone to UTC time."""

from datetime import UTC, datetime, timedelta


def _offset(time: datetime, offset: timedelta) -> datetime:
    return (time - offset).replace(tzinfo=UTC)


def _add_zone(time: datetime) -> datetime:
    return datetime.fromisoformat(time.isoformat() + "+00:00")


def offset_time(time: datetime) -> datetime:
    """Offset date time by current time zone to UTC time.

    If argument "time" is following date time.

    2023-04-16T05:09:30.936886+09:00

    Date time is converted to following value by this function.

    2023-04-15T20:09:30.936886+00:00

    Args:
        time (datetime): Date time object you want to offset.

    Returns:
        datetime: Converted date time to UTC time.

    """
    if (offset := time.utcoffset()) is None:
        return _add_zone(time)

    if timedelta(0) == offset:
        return time

    return _offset(time, offset)
