#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    return _convert_timestamp(
        float(get_file_epoch(path, access=access)), jst=jst
    )


def get_directory_latest(
    walk_generator: PathGene, jst: bool = False, access: bool = False
) -> StrPair:
    return {
        str(path): get_latest(path, jst=jst, access=access).isoformat()
        for path in walk_generator
    }
