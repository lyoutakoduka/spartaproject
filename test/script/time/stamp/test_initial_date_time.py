#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get constant value including time information."""

from decimal import Decimal

from pyspartaproj.script.time.stamp.initial_date_time import get_initial_epoch


def test_epoch() -> None:
    """Test to get UNIX epoch represent April 1, 2023."""
    assert get_initial_epoch() == Decimal("1680307200")
