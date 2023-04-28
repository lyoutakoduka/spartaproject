#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict
from decimal import Decimal
from pathlib import Path

_Default = bool | int | float | str
_Extend = Decimal | Path
_Basic = _Default | _Extend

_DefaultPair = Dict[str, _Default]
_BasicPair = Dict[str, _Basic]
_BoolPair = Dict[str, bool]
_IntPair = Dict[str, int]
_FloatPair = Dict[str, float]
_StrPair = Dict[str, str]
_DecPair = Dict[str, Decimal]
_PathPair = Dict[str, Path]

_Section = \
    _BoolPair | _IntPair | _FloatPair | _StrPair |\
    _DefaultPair

_SectionExtend = \
    _BoolPair | _IntPair | _FloatPair | _StrPair |\
    _DecPair | _PathPair |\
    _BasicPair

Config = Dict[str, _Section]
ConfigExtend = Dict[str, _SectionExtend]
