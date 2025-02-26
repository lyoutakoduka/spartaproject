#!/usr/bin/env python

"""Module to convert data from type Decimal to type float."""

from pyspartalib.context.default.float_context import Floats
from pyspartalib.context.extension.decimal_context import Decs


def convert_float_array(numbers: Decs) -> Floats:
    """Convert array from type Decimal to type float.

    Args:
        numbers (Decs): Decimal array you want to convert.

    Returns:
        Floats: Converted float array.

    """
    return [float(number) for number in numbers]
