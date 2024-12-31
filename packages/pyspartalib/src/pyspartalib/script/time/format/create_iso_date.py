#!/usr/bin/env python

"""Module to convert date time element to several types."""

from datetime import datetime
from decimal import Decimal

from pyspartalib.context.default.integer_context import IntPair2
from pyspartalib.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartalib.script.time.format.format_iso_date import format_iso_date


def _get_groups() -> Strs:
    return ["year", "hour", "zone"]


def _get_types_year() -> Strs:
    return ["year", "month", "day"]


def _get_types_hour() -> Strs:
    return ["hour", "minute", "second"]


def _get_types_zone() -> Strs:
    return ["hour", "minute"]


def _get_types() -> Strs2:
    return [_get_types_year(), _get_types_hour(), _get_types_zone()]


def _get_type_identifiers() -> Strs:
    return ["-"] + [":"] * 2


def _get_group_identifiers() -> Strs:
    return ["T", "+", ""]


def _get_group_string(
    identifier: str,
    key_types: Strs,
    iso_group: StrPair,
) -> str:
    return identifier.join([iso_group[key_type] for key_type in key_types])


def _get_group_strings(string_elements: StrPair2) -> StrPair:
    return {
        group: _get_group_string(identifier, key_types, string_elements[group])
        for group, key_types, identifier in zip(
            _get_groups(),
            _get_types(),
            _get_type_identifiers(),
            strict=True,
        )
        if group in string_elements
    }


def _get_micro(iso_date: StrPair2) -> str | None:
    if "hour" not in iso_date:
        return None

    hour_date = iso_date["hour"]

    if "micro" not in hour_date:
        return None

    return hour_date["micro"]


def _add_micro(string_elements: StrPair2, group_strings: StrPair) -> None:
    if micro := _get_micro(string_elements):
        group_strings["hour"] += "." + micro


def _get_datetime_elements(group_strings: StrPair) -> Strs:
    iso_strings: Strs = []

    for group, identifier in zip(
        _get_groups(),
        _get_group_identifiers(),
        strict=True,
    ):
        if group in group_strings:
            iso_strings += [group_strings[group], identifier]

    return iso_strings[:-1]


def _merge_datetime_elements(group_strings: StrPair) -> str:
    return "".join(_get_datetime_elements(group_strings))


def get_iso_string(iso_date: IntPair2) -> str:
    """Convert date time element to type string.

    e.g., the argument "iso_date" must be following structure.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30, "micro": 123},
        "zone": {"hour": 9, "minute": 0},
    }

    On this case, following date time string in ISO date format is returned.

    "2023-04-01T04:51:30.000123+09:00"

    In addition, following structures are allowed.

    1. No time zone: "2023-04-01T04:51:30.000123" is returned.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30, "micro": 123},
    }

    2. No microsecond value: "2023-04-01T04:51:30+09:00" is returned.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30},
        "zone": {"hour": 9, "minute": 0},
    }

    3. No time zone and microsecond value: "2023-04-01T04:51:30" is returned.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30},
    }

    Args:
        iso_date (IntPair2): Date time element you want to convert.

    Returns:
        str: Get converted date time string.

    """
    string_elements: StrPair2 = format_iso_date(iso_date)
    group_strings: StrPair = _get_group_strings(string_elements)
    _add_micro(string_elements, group_strings)

    return _merge_datetime_elements(group_strings)


def get_iso_time(iso_date: IntPair2) -> datetime:
    """Convert date time element to date time object.

    e.g., the argument "iso_date" must be following structure.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30, "micro": 123},
        "zone": {"hour": 9, "minute": 0},
    }

    On this case, following class "datetime" object is returned.

    datetime(
        2023, 4, 1, 4, 51, 30, 123, tzinfo=timezone(timedelta(seconds=32400))
    )

    Acceptable patterns of input value are same
        as is the case with function "get_iso_string" in current module.

    Args:
        iso_date (IntPair2): Date time element you want to convert.

    Returns:
        datetime: Get converted date time object.

    """
    return datetime.fromisoformat(get_iso_string(iso_date))


def get_iso_epoch(iso_date: IntPair2) -> Decimal:
    """Convert date time element to UNIX epoch.

    e.g., the argument "iso_date" must be following structure.

    {
        "year": {"year": 2023, "month": 4, "day": 1},
        "hour": {"hour": 4, "minute": 51, "second": 30, "micro": 123},
        "zone": {"hour": 9, "minute": 0},
    }

    On this case, following UNIX epoch as class "Decimal" object is returned.

    Decimal('1680292290.000123')

    Acceptable patterns of input value are same
        as is the case with function "get_iso_string" in current module.

    Args:
        iso_date (IntPair2): Date time element you want to convert.

    Returns:
        Decimal: Get converted date time as UNIX epoch.

    """
    return Decimal(str(get_iso_time(iso_date).timestamp()))
