#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import utime
from datetime import datetime

from contexts.path_context import Path
from scripts.times.offset_timezone import offset_time


def set_latest(path: Path, latest_text: str) -> None:
    time_object: datetime = datetime.fromisoformat(offset_time(latest_text))
    utime(path, (path.stat().st_atime, time_object.timestamp()))  # Set as UTC.
