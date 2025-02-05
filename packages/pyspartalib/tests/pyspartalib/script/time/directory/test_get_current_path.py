#!/usr/bin/env python

"""Test module to get path including string of current date time."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.directory.working.working_date_time import (
    get_working_path,
)
from pyspartalib.script.time.directory.get_time_path import (
    get_initial_time_path,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _compare_time_path(result: Path) -> None:
    _difference_error(get_initial_time_path(), result)


def test_name() -> None:
    """Test to get path including string of current date time."""
    _compare_time_path(get_working_path(override=True))
