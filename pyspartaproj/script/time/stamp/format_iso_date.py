#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair2


def _get_iso_digit() -> IntPair2:
    return {
        "year": {"year": 4, "month": 2, "day": 2},
        "hour": {
            "hour": 2,
            "minute": 2,
            "second": 2,
            "millisecond": 6,
        },
        "zone": {"hour": 2, "minute": 2},
    }
