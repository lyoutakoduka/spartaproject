#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get date time about selected file or directory as epoch format."""

from datetime import datetime
from decimal import Decimal
from os import stat_result
from pathlib import Path


def _get_broken_time() -> Decimal:
    broken_time: datetime = datetime.fromisoformat(
        "1980-01-01T00:00:00.000000+00:00"
    )
    return Decimal(str(broken_time.timestamp()))


def get_file_epoch(path: Path, access: bool = False) -> Decimal | None:
    """Get date time about selected file or directory as epoch format.

    Args:
        path (Path): Path of file or directory you want to get date time.

        access (bool, optional): Defaults to False.
            Return update time if it's False, and access time if True.
    Returns:
        Decimal: Latest date time according to condition you select.
    """
    status: stat_result = path.stat()
    time_epoch: Decimal = Decimal(
        str(status.st_atime if access else status.st_mtime)
    )

    if _get_broken_time() >= time_epoch:
        return None

    return time_epoch
