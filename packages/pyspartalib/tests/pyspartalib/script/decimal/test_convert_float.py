#!/usr/bin/env python

"""Test module to convert data from type Decimal to type float."""

from decimal import Decimal

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.float_context import Floats
from pyspartalib.context.extension.decimal_context import Decs
from pyspartalib.script.decimal.convert_float import convert_float_array


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected() -> Floats:
    return [float(i) for i in range(3)]


def _convert_decimal(expected: Floats) -> Decs:
    return [Decimal(str(value)) for value in expected]


def test_array() -> None:
    """Test to convert array from type Decimal to type float."""
    expected: Floats = _get_expected()

    _difference_error(
        convert_float_array(_convert_decimal(expected)),
        expected,
    )
