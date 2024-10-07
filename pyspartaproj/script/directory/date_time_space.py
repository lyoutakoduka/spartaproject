#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create temporary working space including date time string."""

from datetime import datetime
from pathlib import Path

from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints2,
)
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.time.stamp.current_datetime import get_current_time


def _get_source_year(time: datetime) -> IntPair:
    return {"year": time.year, "month": time.month, "day": time.day}


def _get_source_hour(time: datetime) -> IntPair:
    return {
        "hour": time.hour,
        "minute": time.minute,
        "second": time.second,
        "millisecond": time.microsecond,
    }


def _get_source_all(time: datetime) -> IntPair2:
    return {"year": _get_source_year(time), "hour": _get_source_hour(time)}


def _get_time_data(time: datetime) -> Ints2:
    return [
        [4, time.year],
        [2, time.month],
        [2, time.day],
        [2, time.hour],
        [2, time.minute],
        [2, time.second],
        [6, time.microsecond],
    ]


def get_working_space(override: bool = False, jst: bool = False) -> Path:
    """Get path including string of current date time.

    Format of string including date time is follow.

    "<year>/<month>/<day>/<hour>/<second>/<millisecond>"

    And digit for each number follow the rules below.

    Year:           4 digit
    Millisecond:    6 digit
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
    return Path(
        *[
            str(time_count).zfill(order)
            for order, time_count in _get_time_data(
                get_current_time(override=override, jst=jst)
            )
        ]
    )


def create_working_space(
    root: Path, override: bool = False, jst: bool = False
) -> Path:
    """Create temporary working space that path include date time string.

    Args:
        root (Path): Directory path which temporary working space is created.

        override (bool, optional): Defaults to False.
            Override initial time count to "2023/4/1:12:00:00-00 (AM)".
            It's used for argument "override" of function "get_working_space".

        jst (bool, optional): Defaults to False.
            If True, you can get datetime object as JST time zone.
            It's used for argument "jst" of function "get_working_space".

    Returns:
        Path: End of directory path of created temporary working space.
    """
    return create_directory(
        Path(root, get_working_space(override=override, jst=jst))
    )
