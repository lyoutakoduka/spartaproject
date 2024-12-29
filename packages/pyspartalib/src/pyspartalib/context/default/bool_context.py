#!/usr/bin/env python

"""User defined types about type "bool"."""

from typing import Dict, List

Bools = List[bool]
BoolPair = Dict[str, bool]

Bools2 = List[Bools]
BoolPair2 = Dict[str, BoolPair]
BoolType = Bools | BoolPair
