#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal  # not from context
from pathlib import Path  # not from context
from typing import List, Dict

from context.decimal_context import Decs, Decs2, DecPair, DecPair2
from context.default.bool_context import Bools, Bools2, BoolPair, BoolPair2
from context.default.float_context import (
    Floats, Floats2, FloatPair, FloatPair2
)
from context.default.integer_context import Ints, Ints2, IntPair, IntPair2
from context.default.string_context import Strs, Strs2, StrPair, StrPair2
from context.path_context import Paths, Paths2, PathPair, PathPair2

Array = Bools | Ints | Floats | Strs | Decs | Paths
Array2 = Bools2 | Ints2 | Floats2 | Strs2 | Decs2 | Paths2
Pair = BoolPair | IntPair | FloatPair | StrPair | DecPair | PathPair
Pair2 = BoolPair2 | IntPair2 | FloatPair2 | StrPair2 | DecPair2 | PathPair2
Single = None | bool | int | float | str | Decimal | Path

Json = Single | Dict[str, 'Json'] | List['Json']
Multi = Array | Pair
Multi2 = Array2 | Pair2
