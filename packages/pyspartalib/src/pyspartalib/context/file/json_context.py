#!/usr/bin/env python

"""User defined types imitated to file format ".js"."""

from decimal import Decimal
from pathlib import Path
from typing import Dict, List

from pyspartalib.context.default.bool_context import (
    BoolPair,
    BoolPair2,
    Bools,
    Bools2,
)
from pyspartalib.context.default.float_context import (
    FloatPair,
    FloatPair2,
    Floats,
    Floats2,
)
from pyspartalib.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints,
    Ints2,
)
from pyspartalib.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartalib.context.extension.decimal_context import (
    DecPair,
    DecPair2,
    Decs,
    Decs2,
)
from pyspartalib.context.extension.path_context import (
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

Json = Single | dict[str, "Json"] | list["Json"]
Multi = Array | Pair
Multi2 = Array2 | Pair2

Singles = list[Single]
Jsons = list[Json]
