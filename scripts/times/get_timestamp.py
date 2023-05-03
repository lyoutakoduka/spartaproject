#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from datetime import datetime

from scripts.times.from_timestamp import time_from_timestamp


def _convert_timestamp(time: float, jst: bool) -> datetime:
    return time_from_timestamp(Decimal(str(time)), jst=jst)


def get_access(path: Path, jst: bool = False) -> datetime:
    return _convert_timestamp(path.stat().st_atime, jst)


def get_latest(path: Path, jst: bool = False) -> datetime:
    return _convert_timestamp(path.stat().st_mtime, jst)
