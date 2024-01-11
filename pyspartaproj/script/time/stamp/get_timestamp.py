#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get latest date time of file or directory as time object."""

from datetime import datetime
from decimal import Decimal
from pathlib import Path

from pyspartaproj.context.default.string_context import StrPair
from pyspartaproj.context.extension.path_context import PathGene
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.script.time.stamp.from_timestamp import time_from_timestamp
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch


def _convert_timestamp(time: float, jst: bool) -> datetime:
    return time_from_timestamp(Decimal(str(time)), jst=jst)


def _add_latest_stamp(
    path: Path, time: datetime, latest_stamp: TimePair
) -> None:
    latest_stamp[str(path)] = time


def _get_latest_stamp(
    walk_generator: PathGene, jst: bool = False, access: bool = False
) -> StrPair | None:
    latest_stamp: StrPair = {}

    for path in walk_generator:
        if time := get_latest(path, jst=jst, access=access):
            latest_stamp[str(path)] = time.isoformat()
        else:
            return None

    return latest_stamp


def get_latest(
    path: Path, jst: bool = False, access: bool = False
) -> datetime | None:
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
        datetime | None: : Latest date time as time object.
            Return "None" if date time is broke.
    """
    if time := get_file_epoch(path, access=access):
        return _convert_timestamp(float(time), jst=jst)

    return None


def get_directory_latest(
    walk_generator: PathGene, jst: bool = False, access: bool = False
) -> StrPair | None:
    """Get array of latest date time in selected directory as time object.

    Args:
        walk_generator (PathGene):
            Path generator you want to get latest date time inside.

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.

        jst (bool, optional): Defaults to False.
            Return latest date time as JST time zone if it's True.

    Returns:
        StrPair | None:
            Dictionary constructed by string path and latest date time.
            Return "None" if time you got is broke is exists.
    """
    return _get_latest_stamp(walk_generator, jst, access)
