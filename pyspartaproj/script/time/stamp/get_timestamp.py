#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get latest date time of file or directory as time object."""

from datetime import datetime
from decimal import Decimal
from pathlib import Path

from pyspartaproj.context.extension.path_context import PathGene
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.bool.compare_json import is_same_json
from pyspartaproj.script.file.json.convert_to_json import multiple_to_json
from pyspartaproj.script.time.stamp.from_timestamp import time_from_timestamp
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch


def _convert_timestamp(time: float, jst: bool) -> datetime:
    return time_from_timestamp(Decimal(str(time)), jst=jst)


def _add_latest_stamp(
    path: Path, time: datetime, latest_stamp: TimePair
) -> None:
    latest_stamp[str(path)] = time


def _get_latest_stamp(
    walk_generator: PathGene, access: bool = False, jst: bool = False
) -> TimePair:
    latest_stamp: TimePair = {}

    for path in walk_generator:
        if time := get_latest(path, jst=jst, access=access):
            _add_latest_stamp(path, time, latest_stamp)
        else:
            _add_latest_stamp(path, get_invalid_time(), latest_stamp)

    return latest_stamp


def _get_stamp_json(times: TimePair) -> Json:
    return multiple_to_json(
        {path_text: time.isoformat() for path_text, time in times.items()}
    )


def get_invalid_time() -> datetime:
    """Get invalid time date which is used for comparing time you got.

    Returns:
        datetime: Invalid time date.
    """
    return datetime(1, 1, 1)


def get_latest(
    path: Path, access: bool = False, jst: bool = False
) -> datetime:
    """Get latest date time of file or directory as time object.

    Args:
        path (Path): Path of file or directory you want to get date time.
            It's used for argument "path" of function "get_file_epoch".

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.
            It's used for argument "access" of function "get_file_epoch".

        jst (bool, optional): Defaults to False.
            Return latest date time as JST time zone if it's True.

    Returns:
        datetime: Latest date time as time object.
            Return unique invalid time if time you got is broke is exists.
    """
    if time := get_file_epoch(path, access=access):
        return _convert_timestamp(float(time), jst=jst)

    return get_invalid_time()


def is_same_stamp(left: TimePair, right: TimePair) -> bool:
    """Compare 2 dictionaries which store path and time stamp of the path.

    Args:
        left (TimePair): Time stamp of the path you want to compare.

        right (TimePair): Time stamp of the path you want to compare.

    Returns:
        bool: Return True if 2 dictionaries are same value.
    """
    return is_same_json(*[_get_stamp_json(times) for times in [left, right]])


def get_directory_latest(
    walk_generator: PathGene, access: bool = False, jst: bool = False
) -> TimePair:
    """Get array of latest date time in selected directory as time object.

    Args:
        walk_generator (PathGene):
            Path generator you want to get latest date time inside.

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.

        jst (bool, optional): Defaults to False.
            Return latest date time as JST time zone if it's True.

    Returns:
        TimePair: Dictionary constructed by string path and latest date time.
            Return unique invalid time if time you got is broke is exists.
    """
    return _get_latest_stamp(walk_generator, access, jst)
