#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.float_context import Floats
from pyspartaproj.context.extension.decimal_context import Decs


def convert_float_array(numbers: Decs) -> Floats:
    return [float(number) for number in numbers]
