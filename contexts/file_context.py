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

TypeJson = Dict[str, 'TypeJson'] | List['TypeJson'] | _TypeSingle


def _convert_path(content: TypeJson) -> TypeJson:
    return str(content) if isinstance(content, Path) else content


def _convert_decimal(content: TypeJson) -> TypeJson:
    return float(content) if isinstance(content, Decimal) else content


def serialize_json(content: TypeJson) -> TypeJson:
    if isinstance(content, Dict):
        return {key: serialize_json(value) for key, value in content.items()}

    if isinstance(content, List):
        return [serialize_json(value) for value in content]

    return _convert_decimal(_convert_path(content))
