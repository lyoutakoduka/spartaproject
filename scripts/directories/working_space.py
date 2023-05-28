#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from contexts.integer_context import Ints2
from contexts.string_context import Strs
from scripts.paths.create_directory import create_directory
from scripts.paths.get_absolute import get_absolute
from scripts.times.current_datetime import get_current_time


def get_time_data(time: datetime) -> Ints2:
    return [
        [4, time.year],
        [2, time.month],
        [2, time.day],
        [2, time.hour],
        [2, time.minute],
        [2, time.second],
        [6, time.microsecond],
    ]


def current_working_space(
    root: Path, override: bool = False, jst: bool = False,
) -> Path:
    time_texts: Strs = [
        str(time_count).zfill(order)
        for order, time_count in get_time_data(
            get_current_time(override=override, jst=jst)
        )
    ]

    return create_directory(get_absolute(Path(root, *time_texts)))
