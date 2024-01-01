#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get datetime about selected file or directory as epoch format."""

from decimal import Decimal
from os import stat_result
from pathlib import Path


def get_file_epoch(path: Path, access: bool = False) -> Decimal:
    """Get datetime about selected file or directory as epoch format.

    Args:
        path (Path): Path of file or directory you want to get datetime.

        access (bool, optional): Defaults to False.
            Return latest update time, if it's False.
            Return latest access time, if it's True.

    Returns:
        Decimal: Latest datetime according to condition you select.
    """
    status: stat_result = path.stat()
    return Decimal(str(status.st_atime if access else status.st_mtime))
