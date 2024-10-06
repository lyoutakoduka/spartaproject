#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints,
)
from pyspartaproj.context.default.string_context import StrPair, Strs


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


def _format_digit(number: int, digit: int) -> str:
    return str(number).zfill(digit)


def _format_digit_type(source: IntPair, groups: Strs, digits: Ints) -> StrPair:
    return {
        group: _format_digit(source[group], digit)
        for group, digit in zip(groups, digits)
    }


def _get_expected_year() -> StrPair:
    return _format_digit_type(
        _get_source_year(), ["year", "month", "day"], [4] + [2] * 2
    )
