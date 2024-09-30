#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get constant value including time information."""

from decimal import Decimal
from pathlib import Path

from pyspartaproj.script.time.stamp.initial_date_time import (
    get_initial_date_time,
    get_initial_epoch,
)


def test_epoch() -> None:
    """Test to get UNIX epoch represent April 1, 2023."""
    assert get_initial_epoch() == Decimal("1680307200")


def test_utc() -> None:
    """Test to get path represent April 1, 2023 as UTC time zone."""
    assert get_initial_date_time() == Path(
        "2023", "04", "01", "00", "00", "00", "000000"
    )


def test_jst() -> None:
    """Test to get path represent April 1, 2023 as JST time zone."""
    assert get_initial_date_time(jst=True) == Path(
        "2023", "04", "01", "09", "00", "00", "000000"
    )
