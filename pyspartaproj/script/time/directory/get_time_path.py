#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get constant value including time information."""

from pathlib import Path


def _get_hour(jst: bool) -> str:
    return str(9 if jst else 0).zfill(2)


def get_initial_time_path(jst: bool = False) -> Path:
    """Get path represent April 1, 2023.

    You can select time zone from UTC or JST.
    """
    return Path("2023", "04", "01", _get_hour(jst), "00", "00", "000000")
