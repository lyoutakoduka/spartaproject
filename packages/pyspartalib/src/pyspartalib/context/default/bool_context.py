#!/usr/bin/env python

"""User defined types about type "bool"."""

Bools = list[bool]
BoolPair = dict[str, bool]

Bools2 = list[Bools]
BoolPairs = list[BoolPair]
BoolPair2 = dict[str, BoolPair]
BoolType = Bools | BoolPair
