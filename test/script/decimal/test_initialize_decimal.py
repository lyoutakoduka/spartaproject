#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to help calculating by Decimal type."""

from decimal import Context, Decimal, FloatOperation, getcontext, setcontext

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import raises
from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal


def test_float() -> None:
    """Test for assign float to Decimal type directly."""
    with raises(FloatOperation):
        initialize_decimal()
        Decimal(1.0)


def test_accuracy() -> None:
    """Test for accuracy of calculating Decimal type."""

    def get_changed() -> Strs:
        context = getcontext()
        return [str(context.prec), context.rounding]

    setcontext(Context())
    before: Strs = get_changed()
    initialize_decimal()
    after: Strs = get_changed()

    assert before != after
