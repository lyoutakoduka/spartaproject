#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to set latest date time of file or directory by time object."""

from datetime import datetime
from decimal import Decimal
from os import utime
from pathlib import Path

from pyspartaproj.context.default.float_context import Floats
from pyspartaproj.context.extension.decimal_context import Decs
from pyspartaproj.script.decimal.convert_float import convert_float_array
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch
from pyspartaproj.script.time.stamp.offset_timezone import offset_time


def _convert_timestamp(time: datetime) -> Decimal:
    return Decimal(str(offset_time(time).timestamp()))


def _get_path_times(path: Path, time: datetime, access: bool) -> Decs:
    path_times: Decs = [_convert_timestamp(time)]

    if time_epoch := get_file_epoch(path, access=(not access)):
        path_times += [time_epoch]

    if not access:
        path_times.reverse()

    return path_times


def set_latest(path: Path, time: datetime, access: bool = False) -> Path:
    """Set latest date time of file or directory by time object.

    Args:
        path (Path): Path of file or directory you want to set date time.

        time (datetime): Latest date time you want to set.

        access (bool, optional): Defaults to False.
            Set update time if it's False, and access time if True.

    Returns:
        Path: Path of file or directory you set latest date time.
    """
    numbers: Floats = convert_float_array(_get_path_times(path, time, access))
    utime(path, (numbers[0], numbers[1]))

    return path
