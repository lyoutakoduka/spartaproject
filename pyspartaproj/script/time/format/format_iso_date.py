#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.context.default.string_context import StrPair, StrPair2


def _get_digit_year() -> IntPair:
    return {"year": 4, "month": 2, "day": 2}


def _get_digit_hour() -> IntPair:
    return {"hour": 2, "minute": 2, "second": 2, "micro": 6}


def _get_digit_zone() -> IntPair:
    return {"hour": 2, "minute": 2}


def _get_iso_digit() -> IntPair2:
    return {
        "year": _get_digit_year(),
        "hour": _get_digit_hour(),
        "zone": _get_digit_zone(),
    }


def _format_digit(number: int, digit: int) -> str:
    return str(number).zfill(digit)


def _get_formatted_types(
    digit_group: IntPair, number_pair: IntPair
) -> StrPair:
    return {
        number_type: _format_digit(number, digit_group[number_type])
        for number_type, number in number_pair.items()
        if number_type in digit_group
    }


def _get_formatted_groups(
    iso_date_pair: IntPair2, iso_digit: IntPair2
) -> StrPair2:
    return {
        number_group: _get_formatted_types(
            iso_digit[number_group], number_pair
        )
        for number_group, number_pair in iso_date_pair.items()
        if number_group in iso_digit
    }


def format_iso_date(iso_date_pair: IntPair2) -> StrPair2:
    return _get_formatted_groups(iso_date_pair, _get_iso_digit())
