#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get latest datetime of file or directory as time object."""

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
) -> datetime:
    """Get latest datetime of file or directory as time object.

    Args:
        path (Path): Path of file or directory you want to get datetime.
            It's used for argument "path" of function "get_file_epoch".

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.
            It's used for argument "access" of function "get_file_epoch".

        jst (bool, optional): Defaults to False.
            Return latest datetime as JST timezone, if it's True.

    Returns:
        datetime: Latest datetime as time object.
    """
    return _convert_timestamp(
        float(get_file_epoch(path, access=access)), jst=jst
    )


def get_directory_latest(
    walk_generator: PathGene, jst: bool = False, access: bool = False
) -> StrPair:
    """Get array of latest datetime in selected directory as time object.

    Args:
        walk_generator (PathGene):
            Path generator of directory you want to get latest datetime inside.

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.

        jst (bool, optional): Defaults to False.
            Return latest datetime as JST timezone, if it's True.

    Returns:
        StrPair: Dictionary constructed by string path and latest datetime.
    """
    return {
        str(path): get_latest(path, jst=jst, access=access).isoformat()
        for path in walk_generator
    }
