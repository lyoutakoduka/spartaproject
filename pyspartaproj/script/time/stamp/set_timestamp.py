#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from os import utime
from pathlib import Path

from pyspartaproj.script.time.stamp.offset_timezone import offset_time


def _convert_timestamp(time: datetime) -> float:
    time = offset_time(time)
    return time.timestamp()


def set_access(path: Path, time: datetime) -> Path:
    utime(path, (_convert_timestamp(time), path.stat().st_mtime))
    return path


def set_latest(path: Path, time: datetime) -> Path:
    utime(path, (path.stat().st_atime, _convert_timestamp(time)))
    return path
