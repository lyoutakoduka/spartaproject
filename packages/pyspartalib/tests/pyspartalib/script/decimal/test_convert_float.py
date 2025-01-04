#!/usr/bin/env python

"""Test module to convert data from type Decimal to type float."""

from decimal import Decimal

from pyspartalib.context.default.float_context import Floats
from pyspartalib.script.decimal.convert_float import convert_float_array


def _get_expected() -> Floats:
    return [float(i) for i in range(3)]


def test_array() -> None:
    """Test to convert array from type Decimal to type float."""
    expected: Floats = _get_expected()

    if expected != convert_float_array(
        [Decimal(str(value)) for value in expected]
    ):
        raise ValueError
