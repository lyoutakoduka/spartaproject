#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, Generator, List, Tuple

StrPair = Dict[str, str]
StrTuple = Tuple[str, str]
Strs = List[str]
Trans = Dict[int, str]

StrPair2 = Dict[str, StrPair]
Strs2 = List[Strs]

StrGene = Generator[str, None, None]
