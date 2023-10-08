#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Context, Decimal, FloatOperation, getcontext, setcontext

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.decimal_context import set_decimal_context
from pyspartaproj.interface.pytest import raises


def test_float() -> None:
    with raises(FloatOperation):
        set_decimal_context()
        Decimal(1.0)


def test_accuracy() -> None:
    def get_changed() -> Strs:
        context = getcontext()
        return [str(context.prec), context.rounding]

    setcontext(Context())
    before: Strs = get_changed()
    set_decimal_context()
    after: Strs = get_changed()

    assert before != after


def main() -> bool:
    test_accuracy()
    test_float()
    return True
