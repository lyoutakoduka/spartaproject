#!/usr/bin/env python

"""User defined types imitated to file format ".ini"."""

from decimal import Decimal
from pathlib import Path

from pyspartalib.context.default.bool_context import BoolPair, BoolPair2
from pyspartalib.context.default.float_context import FloatPair, FloatPair2
from pyspartalib.context.default.integer_context import IntPair, IntPair2
from pyspartalib.context.default.string_context import StrPair, StrPair2
from pyspartalib.context.extension.decimal_context import DecPair, DecPair2
from pyspartalib.context.extension.path_context import PathPair, PathPair2

Single = bool | int | float | str | Decimal | Path

SinglePair = dict[str, Single]
SectionPair = BoolPair | IntPair | FloatPair | DecPair | StrPair | PathPair

SinglePair2 = dict[str, SinglePair]
SectionPair2 = dict[str, SectionPair]

Config = (
    BoolPair2
    | IntPair2
    | FloatPair2
    | DecPair2
    | StrPair2
    | PathPair2
    | SinglePair2
    | SectionPair2
)
