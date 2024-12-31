#!/usr/bin/env python

"""Module to get date time about selected file or directory as epoch format."""

from decimal import Decimal
from os import stat_result
from pathlib import Path

from pyspartalib.context.default.integer_context import IntPair2
from pyspartalib.script.time.format.create_iso_date import get_iso_epoch


def _to_decimal(number: float) -> Decimal:
    return Decimal(str(number))


def _get_access_date(path: Path) -> Decimal:
    return _to_decimal(path.stat().st_atime)


def _get_source() -> IntPair2:
    return {
        "year": {"year": 1980, "month": 1, "day": 1},
        "hour": {"hour": 0, "minute": 0, "second": 0, "micro": 0},
        "zone": {"hour": 0, "minute": 0},
    }


def _get_epoch_source(path: Path, access: bool) -> Decimal:
    status: stat_result = path.stat()
    return Decimal(str(status.st_atime if access else status.st_mtime))


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
    time_epoch: Decimal = _get_epoch_source(path, access)

    if get_iso_epoch(_get_source()) >= time_epoch:
        return None

    return time_epoch
