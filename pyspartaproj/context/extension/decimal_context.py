#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types about type "Decimal"."""

from decimal import Decimal
from typing import Dict, List

DecPair = Dict[str, Decimal]
Decs = List[Decimal]

DecPair2 = Dict[str, DecPair]
Decs2 = List[Decs]
