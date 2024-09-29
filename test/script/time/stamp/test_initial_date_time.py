#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal

from pyspartaproj.script.time.stamp.initial_date_time import get_initial_epoch


def test_epoch() -> None:
    assert get_initial_epoch() == Decimal("1680307200")
