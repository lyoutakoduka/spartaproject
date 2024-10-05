#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types imitated to file format ".js"."""

from decimal import Decimal
from pathlib import Path
from typing import Dict, List

from pyspartaproj.context.default.bool_context import (
    BoolPair,
    BoolPair2,
    Bools,
    Bools2,
)
from pyspartaproj.context.default.float_context import (
    FloatPair,
    FloatPair2,
    Floats,
    Floats2,
)
from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints,
    Ints2,
)
from pyspartaproj.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartaproj.context.extension.decimal_context import (
    DecPair,
    DecPair2,
    Decs,
    Decs2,
)
from pyspartaproj.context.extension.path_context import (
    PathPair,
    PathPair2,
    Paths,
    Paths2,
)

Array = Bools | Ints | Floats | Strs | Decs | Paths
Array2 = Bools2 | Ints2 | Floats2 | Strs2 | Decs2 | Paths2
Pair = BoolPair | IntPair | FloatPair | StrPair | DecPair | PathPair
Pair2 = BoolPair2 | IntPair2 | FloatPair2 | StrPair2 | DecPair2 | PathPair2
Single = None | bool | int | float | str | Decimal | Path

Json = Single | Dict[str, "Json"] | List["Json"]
Multi = Array | Pair
Multi2 = Array2 | Pair2

Jsons = List[Json]
