#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import Dict, Union

Basic = bool | int | float | str | Decimal | Path

_BasicPair = Dict[str, Basic]
_BoolPair = Dict[str, bool]
_DecPair = Dict[str, Decimal]
_FloatPair = Dict[str, float]
_IntPair = Dict[str, int]
_PathPair = Dict[str, Path]
_StrPair = Dict[str, str]

_Section = Union[
    _BoolPair, _IntPair, _FloatPair, _StrPair, _DecPair, _PathPair, _BasicPair
]

_BasicPair2 = Dict[str, _Section]
_BoolPair2 = Dict[str, _BoolPair]
_DecPair2 = Dict[str, _DecPair]
_FloatPair2 = Dict[str, _FloatPair]
_IntPair2 = Dict[str, _IntPair]
_PathPair2 = Dict[str, _PathPair]
_StrPair2 = Dict[str, _StrPair]

Config = Union[
    _BoolPair2,
    _IntPair2,
    _FloatPair2,
    _StrPair2,
    _DecPair2,
    _PathPair2,
    _BasicPair2,
]
