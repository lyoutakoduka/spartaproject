#!/usr/bin/env python

"""Module to get constant value including time information."""

from decimal import Decimal


def get_initial_epoch() -> Decimal:
    """Get UNIX epoch represent April 1, 2023."""
    return Decimal("1680307200")
