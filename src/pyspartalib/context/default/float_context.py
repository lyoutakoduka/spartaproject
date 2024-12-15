#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types about type "float"."""

from typing import Dict, List

FloatPair = Dict[str, float]
Floats = List[float]

FloatPair2 = Dict[str, FloatPair]
Floats2 = List[Floats]
