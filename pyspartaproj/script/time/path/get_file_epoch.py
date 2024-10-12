#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get date time about selected file or directory as epoch format."""

from datetime import datetime
from decimal import Decimal
from os import stat_result
from pathlib import Path

from pyspartaproj.context.default.integer_context import IntPair2
from pyspartaproj.script.time.format.create_iso_date import create_iso_date


def _get_source() -> IntPair2:
    return {
        "year": {"year": 1980, "month": 1, "day": 1},
        "hour": {"hour": 0, "minute": 0, "second": 0, "millisecond": 0},
        "zone": {"hour": 0, "minute": 0},
    }


def _get_date_time() -> datetime:
    return datetime.fromisoformat(create_iso_date(_get_source()))


def _get_broken_time() -> Decimal:
    return Decimal(str(_get_date_time().timestamp()))


def get_file_epoch(path: Path, access: bool = False) -> Decimal | None:
    """Get date time about selected file or directory as epoch format.

    Args:
        path (Path): Path of file or directory you want to get date time.

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.

    Returns:
        Decimal | None: Latest date time according to condition you select.
            Return "None" if date time is broke.
    """
    status: stat_result = path.stat()
    time_epoch: Decimal = Decimal(
        str(status.st_atime if access else status.st_mtime)
    )

    if _get_broken_time() >= time_epoch:
        return None

    return time_epoch
