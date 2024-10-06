#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair, IntPair2


def _get_source_year() -> IntPair:
    return {"year": 2023, "month": 4, "day": 1}


def _get_source_hour() -> IntPair:
    return {"hour": 4, "minute": 51, "second": 30, "millisecond": 123}


def _get_source_zone() -> IntPair:
    return {"hour": 9, "minute": 15}


def _get_source_all() -> IntPair2:
    return {
        "year": _get_source_year(),
        "hour": _get_source_hour(),
        "zone": _get_source_zone(),
    }
