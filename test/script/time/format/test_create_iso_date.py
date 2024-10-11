#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair


def _get_years() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_hours() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30, "millisecond": 123}
