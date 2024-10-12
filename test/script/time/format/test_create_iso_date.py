#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair, IntPair2


def _get_years() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_hours() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30, "millisecond": 123}


def _get_second() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30}


def _get_zones() -> IntPair:
    return {"hour": 9, "minute": 15}


def _get_source_all() -> IntPair2:
    return {"year": _get_years(), "hour": _get_hours(), "zone": _get_zones()}


def _get_source_millisecond() -> IntPair2:
    return {"year": _get_years(), "hour": _get_second(), "zone": _get_zones()}
