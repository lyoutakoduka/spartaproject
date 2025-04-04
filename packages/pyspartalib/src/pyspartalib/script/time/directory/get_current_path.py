#!/usr/bin/env python

"""Module to get path including string of current date time."""

from datetime import datetime
from pathlib import Path

from pyspartalib.context.default.integer_context import IntPair2
from pyspartalib.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartalib.script.time.format.format_iso_date import format_iso_date
from pyspartalib.script.time.stamp.current_datetime import get_current_time


def _get_source_all(time: datetime) -> IntPair2:
    return {
        "year": {"year": time.year, "month": time.month, "day": time.day},
        "hour": {
            "hour": time.hour,
            "minute": time.minute,
            "second": time.second,
            "micro": time.microsecond,
        },
    }


def _get_result_groups() -> Strs:
    return ["year", "hour"]


def _get_result_year() -> Strs:
    return ["year", "month", "day"]


def _get_result_hour() -> Strs:
    return ["hour", "minute", "second", "micro"]


def _get_result_types() -> Strs2:
    return [_get_result_year(), _get_result_hour()]


def _sort_result(result: StrPair, result_types: Strs) -> Strs:
    return [result[result_type] for result_type in result_types]


def _sort_formatted(result_all: StrPair2) -> Strs:
    return [
        result
        for result_group, result_types in zip(
            _get_result_groups(),
            _get_result_types(),
            strict=True,
        )
        for result in _sort_result(result_all[result_group], result_types)
    ]


def _get_formatted(override: bool, jst: bool) -> StrPair2:
    return format_iso_date(
        _get_source_all(get_current_time(override=override, jst=jst)),
    )


def get_working_path(override: bool = False, jst: bool = False) -> Path:
    """Get path including string of current date time.

    Format of string including date time is follow.

    "<year>/<month>/<day>/<hour>/<second>/<microsecond>"

    And digit for each number follow the rules below.

    Year:           4 digit
    Microsecond:    6 digit
    Other:          2 digit

    Return directory path including string like "2023/04/01/00/00/00/000000",
        if you execute this function at 2024/1/1:12:00:00-00 (AM).

    Args:
        override (bool, optional): Defaults to False.
            Override initial time count to "2023/4/1:12:00:00-00 (AM)".
            It's used for argument "override" of function "get_current_time".

        jst (bool, optional): Defaults to False.
            If True, you can get datetime object as JST time zone.
            It's used for argument "jst" of function "get_current_time".

    Returns:
        Path: Path including string of current date time.

    """
    return Path(*_sort_formatted(_get_formatted(override, jst)))
