#!/usr/bin/env python

"""User defined types about type "str"."""

from collections.abc import Generator

StrPair = dict[str, str]
StrTuple = tuple[str, str]
Strs = list[str]
Trans = dict[int, str]

StrsPair = dict[str, Strs]
StrPair2 = dict[str, StrPair]
Strs2 = list[Strs]

StrGene = Generator[str]
Strs3 = list[Strs2]
