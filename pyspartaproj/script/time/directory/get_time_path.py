#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get constant value including time information."""

from pathlib import Path


def get_initial_time_path(jst: bool = False) -> Path:
    """Get path represent April 1, 2023.

    You can select time zone from UTC or JST.
    """
    return Path(
        "2023", "04", "01", str(9 if jst else 0).zfill(2), "00", "00", "000000"
    )