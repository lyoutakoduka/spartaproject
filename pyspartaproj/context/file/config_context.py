#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types imitated to file format ".ini"."""

from decimal import Decimal
from pathlib import Path
from typing import Dict, Union

Basic = bool | int | float | str | Decimal | Path

_BoolPair = Dict[str, bool]
_IntPair = Dict[str, int]
_FloatPair = Dict[str, float]
_DecPair = Dict[str, Decimal]
_StrPair = Dict[str, str]
_PathPair = Dict[str, Path]
BasicPair = Dict[str, Basic]

SectionPair = Union[
    _BoolPair, _IntPair, _FloatPair, _DecPair, _StrPair, _PathPair
]

_BoolPair2 = Dict[str, _BoolPair]
_IntPair2 = Dict[str, _IntPair]
_FloatPair2 = Dict[str, _FloatPair]
_DecPair2 = Dict[str, _DecPair]
_StrPair2 = Dict[str, _StrPair]
_PathPair2 = Dict[str, _PathPair]
BasicPair2 = Dict[str, BasicPair]
SectionPair2 = Dict[str, SectionPair]

Config = Union[
    _BoolPair2,
    _IntPair2,
    _FloatPair2,
    _DecPair2,
    _StrPair2,
    _PathPair2,
    BasicPair2,
    SectionPair2,
]
