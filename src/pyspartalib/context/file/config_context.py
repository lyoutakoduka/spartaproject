#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types imitated to file format ".ini"."""

from decimal import Decimal
from pathlib import Path
from typing import Dict, Union

from pyspartalib.context.default.bool_context import BoolPair, BoolPair2
from pyspartalib.context.default.float_context import FloatPair, FloatPair2
from pyspartalib.context.default.integer_context import IntPair, IntPair2
from pyspartalib.context.default.string_context import StrPair, StrPair2
from pyspartalib.context.extension.decimal_context import DecPair, DecPair2
from pyspartalib.context.extension.path_context import PathPair, PathPair2

Basic = bool | int | float | str | Decimal | Path

BasicPair = Dict[str, Basic]
SectionPair = Union[BoolPair, IntPair, FloatPair, DecPair, StrPair, PathPair]

BasicPair2 = Dict[str, BasicPair]
SectionPair2 = Dict[str, SectionPair]

Config = Union[
    BoolPair2,
    IntPair2,
    FloatPair2,
    DecPair2,
    StrPair2,
    PathPair2,
    BasicPair2,
    SectionPair2,
]
