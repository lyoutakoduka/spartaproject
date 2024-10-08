#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get constant value including time information."""

from pathlib import Path

from pyspartaproj.script.time.directory.get_time_path import (
    get_initial_time_path,
)


def test_utc() -> None:
    """Test to get path represent April 1, 2023 as UTC time zone."""
    assert get_initial_time_path() == Path(
        "2023", "04", "01", "00", "00", "00", "000000"
    )


def test_jst() -> None:
    """Test to get path represent April 1, 2023 as JST time zone."""
    assert get_initial_time_path(jst=True) == Path(
        "2023", "04", "01", "09", "00", "00", "000000"
    )
