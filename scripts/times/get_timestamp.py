#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from datetime import datetime

from scripts.times.from_timestamp import time_from_timestamp


def get_latest(path: Path, jst: bool = False) -> datetime:
    return time_from_timestamp(Decimal(str(path.stat().st_mtime)))
