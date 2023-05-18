#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict, Union

Single = None | bool | int | float | str | Decimal | Path

Json = Single | Dict[str, 'Json'] | List['Json']

Array = Union[
    List[bool],
    List[int],
    List[float],
    List[str],
    List[Decimal],
    List[Path],
]

Pair = Union[
    Dict[str, bool],
    Dict[str, int],
    Dict[str, float],
    Dict[str, str],
    Dict[str, Decimal],
    Dict[str, Path],
]

Array2 = List[Array]
Pair2 = Dict[str, Pair]
