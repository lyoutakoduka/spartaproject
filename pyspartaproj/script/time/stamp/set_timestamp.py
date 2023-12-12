#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal
from os import utime
from pathlib import Path

from pyspartaproj.context.default.float_context import Floats
from pyspartaproj.context.extension.decimal_context import Decs
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch
from pyspartaproj.script.time.stamp.offset_timezone import offset_time


def _convert_timestamp(time: datetime) -> float:
    time = offset_time(time)
    return time.timestamp()


def set_latest(path: Path, time: datetime, access: bool = False) -> Path:
    path_times: Decs = [
        Decimal(str(_convert_timestamp(time))),
        get_file_epoch(path, access=(not access)),
    ]

    if not access:
        path_times.reverse()

    path_numbers: Floats = [float(path_time) for path_time in path_times]
    utime(path, (path_numbers[0], path_numbers[1]))

    return path
