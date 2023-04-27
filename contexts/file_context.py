#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

_Bools = List[bool]
_BoolPair = Dict[str, bool]
_BoolsList = List[_Bools]
_TypeBool = _Bools | _BoolPair | _BoolsList

_Ints = List[int]
_IntPair = Dict[str, int]
_IntsList = List[_Ints]
_TypeInt = _Ints | _IntPair | _IntsList

_Floats = List[float]
_FloatPair = Dict[str, float]
_TypeFloat = _Floats | _FloatPair

_Decs = List[Decimal]
_DecPair = Dict[str, Decimal]
_TypeDec = Decimal | _Decs | _DecPair

_Strs = List[str]
_StrPair = Dict[str, str]
_StrList = List[_Strs]
_StrPair2 = Dict[str, _StrPair]
_TypeStr = _Strs | _StrPair | _StrList | _StrPair2

_Paths = List[Path]
_PathPair = Dict[str, Path]
_TypePath = Path | _Paths | _PathPair

_TypeDefault = str | int | float | bool | None
_TypeUser = _TypePath | _TypeStr | _TypeDec | _TypeFloat | _TypeInt | _TypeBool
_TypeSingle = _TypeDefault | _TypeUser

TypeFile = Dict[str, 'TypeFile'] | List['TypeFile'] | _TypeSingle


def serialize_unknown(content: TypeFile) -> TypeFile:
    if isinstance(content, Dict):
        return {key: serialize_unknown(value) for key, value in content.items()}

    if isinstance(content, List):
        return [serialize_unknown(value) for value in content]

    if isinstance(content, Path):
        return str(content)

    if isinstance(content, Decimal):
        return float(content)

    return content
