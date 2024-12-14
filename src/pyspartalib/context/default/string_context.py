#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types about type "str"."""

from typing import Dict, Generator, List, Tuple

StrPair = Dict[str, str]
StrTuple = Tuple[str, str]
Strs = List[str]
Trans = Dict[int, str]

StrsPair = Dict[str, Strs]
StrPair2 = Dict[str, StrPair]
Strs2 = List[Strs]

StrGene = Generator[str, None, None]
Strs3 = List[Strs2]
