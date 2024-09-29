#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path


def get_initial_epoch() -> Decimal:
    return Decimal("1680307200")


def get_initial_date_time(jst: bool = False) -> Path:
    return Path(
        "2023", "04", "01", str(9 if jst else 0).zfill(2), "00", "00", "000000"
    )
