#!/usr/bin/env python

"""Module to help calculating by type Decimal."""

from decimal import ROUND_FLOOR, Context, FloatOperation, setcontext


def initialize_decimal() -> None:
    """Execute before calculating type Decimal."""
    context: Context = Context(prec=32, rounding=ROUND_FLOOR)
    context.traps[FloatOperation] = True
    setcontext(context)
