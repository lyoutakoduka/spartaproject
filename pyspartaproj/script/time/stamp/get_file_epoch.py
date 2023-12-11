#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from os import stat_result
from pathlib import Path


def get_file_epoch(path: Path, access: bool = False) -> Decimal:
    status: stat_result = path.stat()
    return Decimal(str(status.st_atime if access else status.st_mtime))
