#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict

Bools = List[bool]
BoolPair = Dict[str, bool]

Bools2 = List[Bools]
BoolPair2 = Dict[str, BoolPair]
BoolType = Bools | BoolPair
