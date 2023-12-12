#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal

from pyspartaproj.context.default.float_context import Floats
from pyspartaproj.script.decimal.convert_float import convert_float_array


def test_array() -> None:
    expected: Floats = [float(i) for i in range(3)]
    assert expected == convert_float_array(
        [Decimal(str(value)) for value in expected]
    )


def main() -> bool:
    test_array()
    return True
