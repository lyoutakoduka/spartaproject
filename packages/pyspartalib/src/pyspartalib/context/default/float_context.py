#!/usr/bin/env python

"""User defined types about type "float"."""

from typing import Dict, List

FloatPair = dict[str, float]
Floats = list[float]

FloatPair2 = dict[str, FloatPair]
Floats2 = list[Floats]
