#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path

from pyspartaproj.script.time.stamp.initial_date_time import (
    get_initial_date_time,
    get_initial_epoch,
)


def test_epoch() -> None:
    assert get_initial_epoch() == Decimal("1680307200")


def test_utc() -> None:
    assert get_initial_date_time() == Path(
        "2023", "04", "01", "00", "00", "00", "000000"
    )
