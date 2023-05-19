#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

Single = None | bool | int | float | str | Decimal | Path

Json = Single | Dict[str, 'Json'] | List['Json']

_BoolPair = Dict[str, bool]
_Bools = List[bool]
_DecPair = Dict[str, Decimal]
_Decs = List[Decimal]
_FloatPair = Dict[str, float]
_Floats = List[float]
_IntPair = Dict[str, int]
_Ints = List[int]
_PathPair = Dict[str, Path]
_Paths = List[Path]
_StrPair = Dict[str, str]
_Strs = List[str]

Array = _Bools | _Ints | _Floats | _Strs | _Decs | _Paths
Pair = _BoolPair | _IntPair | _FloatPair | _StrPair | _DecPair | _PathPair

_BoolPair2 = Dict[str, _BoolPair]
_Bools2 = List[_Bools]
_DecPair2 = Dict[str, _DecPair]
_Decs2 = List[_Decs]
_FloatPair2 = Dict[str, _FloatPair]
_Floats2 = List[_Floats]
_IntPair2 = Dict[str, _IntPair]
_Ints2 = List[_Ints]
_PathPair2 = Dict[str, _PathPair]
_Paths2 = List[_Paths]
_StrPair2 = Dict[str, _StrPair]
_Strs2 = List[_Strs]

Array2 = _Bools2 | _Ints2 | _Floats2 | _Strs2 | _Decs2 | _Paths2
Pair2 = _BoolPair2 | _IntPair2 | _FloatPair2 | _StrPair2 | _DecPair2 | _PathPair2
