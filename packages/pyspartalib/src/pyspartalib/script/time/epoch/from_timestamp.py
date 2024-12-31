#!/usr/bin/env python

"""Module to convert time data from epoch format to datetime object."""

from datetime import datetime
from decimal import Decimal

from pyspartalib.interface.dateutil.tz import gettz


def time_from_timestamp(timestamp: Decimal, jst: bool = False) -> datetime:
    """Convert time data from epoch format to datetime object.

    Args:
        timestamp (Decimal): Epoch format time you want to convert.

        jst (bool, optional): Defaults to False.
            If True, you can get datetime object as JST time zone.

    Returns:
        datetime: Converted datetime object.
    """
    date_time: datetime = datetime.fromtimestamp(float(timestamp))
    return date_time.astimezone(gettz("Asia/Tokyo" if jst else "UTC"))
