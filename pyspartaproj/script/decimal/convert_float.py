#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert data from type Decimal to type float."""

from pyspartaproj.context.default.float_context import Floats
from pyspartaproj.context.extension.decimal_context import Decs


def convert_float_array(numbers: Decs) -> Floats:
    """Function to convert array from type Decimal to type float.

    Args:
        numbers (Decs): Decimal array you want to convert.

    Returns:
        Floats: Converted float array.
    """
    return [float(number) for number in numbers]
