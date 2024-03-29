#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from pyspartaproj.context.default.integer_context import Ints2
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.time.current_datetime import get_current_time


def _get_time_data(time: datetime) -> Ints2:
    return [
        [4, time.year],
        [2, time.month],
        [2, time.day],
        [2, time.hour],
        [2, time.minute],
        [2, time.second],
        [6, time.microsecond],
    ]


def get_working_space(override: bool = False, jst: bool = False) -> Path:
    return Path(
        *[
            str(time_count).zfill(order)
            for order, time_count in _get_time_data(
                get_current_time(override=override, jst=jst)
            )
        ]
    )


def create_working_space(
    root: Path, override: bool = False, jst: bool = False
) -> Path:
    return create_directory(
        Path(root, get_working_space(override=override, jst=jst))
    )
