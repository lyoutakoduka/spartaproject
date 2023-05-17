#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict
from decimal import Decimal
from pathlib import Path

_Default = bool | int | float | str
_Extend = Decimal | Path

Basic = _Default | _Extend

_BasicPair = Dict[str, Basic]
_BoolPair = Dict[str, bool]
_DecPair = Dict[str, Decimal]
_FloatPair = Dict[str, float]
_IntPair = Dict[str, int]
_PathPair = Dict[str, Path]
_StrPair = Dict[str, str]

_Section = \
    _BoolPair | _IntPair | _FloatPair | _StrPair |\
    _DecPair | _PathPair |\
    _BasicPair

Config = Dict[str, _Section]
