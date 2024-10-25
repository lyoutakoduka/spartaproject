#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get constant value including time information."""

from pathlib import Path

from pyspartaproj.script.time.directory.get_time_path import (
    get_initial_time_path,
)


def _get_hour(jst: bool) -> str:
    return str(9 if jst else 0).zfill(2)


def _get_time_path(jst: bool = False) -> Path:
    return Path("2023", "04", "01", _get_hour(jst), "00", "00", "000000")


def test_utc() -> None:
    """Test to get path represent April 1, 2023 as UTC time zone."""
    assert get_initial_time_path() == _get_time_path()


def test_jst() -> None:
    """Test to get path represent April 1, 2023 as JST time zone."""
    assert get_initial_time_path(jst=True) == _get_time_path(jst=True)
