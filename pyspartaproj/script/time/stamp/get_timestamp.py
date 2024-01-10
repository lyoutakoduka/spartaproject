#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get latest date time of file or directory as time object."""

from datetime import datetime
from decimal import Decimal
from pathlib import Path

from pyspartaproj.context.default.string_context import StrPair
from pyspartaproj.context.extension.path_context import PathGene
from pyspartaproj.script.time.stamp.from_timestamp import time_from_timestamp
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch


def _convert_timestamp(time: float, jst: bool) -> datetime:
    return time_from_timestamp(Decimal(str(time)), jst=jst)


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
            Return latest date time as JST time zone, if it's True.

    Returns:
        datetime: Latest date time as time object.
    """
    if time := get_file_epoch(path, access=access):
        return _convert_timestamp(float(time), jst=jst)

    return None


def get_directory_latest(
    walk_generator: PathGene, jst: bool = False, access: bool = False
) -> StrPair:
    """Get array of latest date time in selected directory as time object.

    Args:
        walk_generator (PathGene):
            Path generator you want to get latest date time inside.

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.

        jst (bool, optional): Defaults to False.
            Return latest date time as JST time zone, if it's True.

    Returns:
        StrPair: Dictionary constructed by string path and latest date time.
    """
    return {
        str(path): get_latest(path, jst=jst, access=access).isoformat()
        for path in walk_generator
    }
