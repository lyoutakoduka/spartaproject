#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert date time element from type number to string."""

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


def _get_formatted_groups(iso_date: IntPair2, iso_digit: IntPair2) -> StrPair2:
    return {
        number_group: _get_formatted_types(
            iso_digit[number_group], number_pair
        )
        for number_group, number_pair in iso_date.items()
        if number_group in iso_digit
    }


def format_iso_date(iso_date: IntPair2) -> StrPair2:
    """Convert date time element from type number to string.

    e.g., the argument "iso_date" must be following structure.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30, "micro": 123},
        "zone": {"hour": 9, "minute": 0},
    }

    On this case,
        following date time element structured by type string is returned.

    {
        "year": {"year": "2023", "month": "04", "day": "01"},
        "hour": {
            "hour": "04",
            "minute": "51",
            "second": "30",
            "micro": "000123",
        },
        "zone": {"hour": "09", "minute": "00"},
    }

    Digits of each numbers in the element are determined by following rule.

    iso_date["year"]["year"]: 4
    iso_date["hour"]["year"]: 2
    iso_date["day"]["year"]: 2

    iso_date["hour"]["hour"]: 2
    iso_date["minute"]["hour"]: 2
    iso_date["second"]["hour"]: 2
    iso_date["micro"]["hour"]: 6

    iso_date["hour"]["zone"]: 2
    iso_date["minute"]["zone"]: 2

    Args:
        iso_date_pair (IntPair2): Date time element you want to convert.

    Returns:
        StrPair2: Get converted date time element structured by type string.
    """
    return _get_formatted_groups(iso_date, _get_iso_digit())
