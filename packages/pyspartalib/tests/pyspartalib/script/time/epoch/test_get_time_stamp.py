#!/usr/bin/env python

"""Test module to get constant value including time information."""

from decimal import Decimal

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.time.epoch.get_time_stamp import get_initial_epoch


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def test_epoch() -> None:
    """Test to get UNIX epoch represent April 1, 2023."""
    _difference_error(get_initial_epoch(), Decimal("1680307200"))
