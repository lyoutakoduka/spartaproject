#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.integer_context import IntPair2
from pyspartaproj.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartaproj.script.time.format.format_iso_date import format_iso_date


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
    identifier: str, key_types: Strs, iso_group: StrPair
) -> str:
    return identifier.join([iso_group[key_type] for key_type in key_types])


def _get_group_strings(iso_date: StrPair2) -> StrPair:
    return {
        group: _get_group_string(identifier, key_types, iso_date[group])
        for group, key_types, identifier in zip(
            _get_groups(), _get_types(), _get_type_identifiers()
        )
        if group in iso_date
    }


def _get_millisecond(iso_date: StrPair2) -> str | None:
    if "hour" in iso_date:
        hour_date = iso_date["hour"]

        if "millisecond" in hour_date:
            return hour_date["millisecond"]

    return None


def _merge_hour_elements(millisecond: str, group_strings: StrPair) -> str:
    return group_strings["hour"] + "." + millisecond


def _merge_elements(hour: str, group_strings: StrPair) -> str:
    return group_strings["year"] + "T" + hour + "+" + group_strings["zone"]


def _create_string(iso_date: StrPair2, group_strings: StrPair) -> str:
    return _merge_elements(
        _merge_hour_elements(_get_millisecond(iso_date), group_strings),
        group_strings,
    )


def create_iso_date(iso_date_pair: IntPair2) -> str:
    iso_date: StrPair2 = format_iso_date(iso_date_pair)
    return _create_string(iso_date, _get_group_strings(iso_date))
