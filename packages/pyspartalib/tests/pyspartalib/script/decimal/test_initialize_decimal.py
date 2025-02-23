#!/usr/bin/env python

"""Test module to help calculating by Decimal type."""

from decimal import Context, Decimal, FloatOperation, getcontext, setcontext

import pytest
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal


def _compute_decimal() -> None:
    initialize_decimal()

    number: float = 1.0
    Decimal(number)


def test_float() -> None:
    """Test for assign float to Decimal type directly."""
    with pytest.raises(FloatOperation):
        _compute_decimal()


def test_accuracy() -> None:
    """Test for accuracy of calculating Decimal type."""

    def get_changed() -> Strs:
        context = getcontext()
        return [str(context.prec), context.rounding]

    setcontext(Context())
    before: Strs = get_changed()

    initialize_decimal()
    after: Strs = get_changed()

    if before == after:
        raise ValueError
