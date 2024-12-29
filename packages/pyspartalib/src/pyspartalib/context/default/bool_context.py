#!/usr/bin/env python

"""User defined types about type "bool"."""

Bools = list[bool]
BoolPair = dict[str, bool]

Bools2 = list[Bools]
BoolPair2 = dict[str, BoolPair]
BoolType = Bools | BoolPair
