#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types about type "int"."""

from typing import Dict, List, Tuple

IntPair = Dict[str, int]
Ints = List[int]
IntTuple = Tuple[int, ...]

IntPair2 = Dict[str, IntPair]
Ints2 = List[Ints]

Ints3 = List[Ints2]
IntPair3 = Dict[str, IntPair2]
