#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get path including string of current date time."""

from pathlib import Path

from pyspartaproj.script.directory.date_time_space import get_working_space
from pyspartaproj.script.time.path.get_time_path import get_initial_time_path


def _compare_time_path(result: Path) -> None:
    assert get_initial_time_path() == result


def test_name() -> None:
    """Test to get path including string of current date time."""
    _compare_time_path(get_working_space(override=True))
