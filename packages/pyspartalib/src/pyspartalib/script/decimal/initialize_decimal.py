#!/usr/bin/env python

"""Module to help calculating by Decimal type."""

from decimal import ROUND_FLOOR, Context, FloatOperation, setcontext


def initialize_decimal() -> None:
    """Function must running before calculating Decimal type."""
    context: Context = Context(prec=32, rounding=ROUND_FLOOR)
    context.traps[FloatOperation] = True
    setcontext(context)
