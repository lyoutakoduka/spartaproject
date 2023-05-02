#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import utime
from pathlib import Path
from datetime import datetime

from scripts.times.offset_timezone import offset_time


def set_latest(path: Path, latest: str) -> None:
    time_object: datetime = datetime.fromisoformat(offset_time(latest))
    utime(path, (path.stat().st_atime, time_object.timestamp()))  # Set as UTC.
