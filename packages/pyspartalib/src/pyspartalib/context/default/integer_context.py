#!/usr/bin/env python

"""User defined types about type "int"."""

from typing import Dict, List, Tuple

IntPair = dict[str, int]
Ints = list[int]
IntTuple = tuple[int, ...]

IntPair2 = dict[str, IntPair]
Ints2 = list[Ints]

Ints3 = list[Ints2]
IntPair3 = dict[str, IntPair2]
