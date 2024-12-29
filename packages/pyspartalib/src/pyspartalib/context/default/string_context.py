#!/usr/bin/env python

"""User defined types about type "str"."""

from typing import Dict, Generator, List, Tuple

StrPair = dict[str, str]
StrTuple = tuple[str, str]
Strs = list[str]
Trans = dict[int, str]

StrsPair = dict[str, Strs]
StrPair2 = dict[str, StrPair]
Strs2 = list[Strs]

StrGene = Generator[str, None, None]
Strs3 = list[Strs2]
