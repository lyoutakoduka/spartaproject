#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import ROUND_FLOOR, Context, Decimal, FloatOperation, setcontext
from typing import Dict, List

DecPair = Dict[str, Decimal]
Decs = List[Decimal]

DecPair2 = Dict[str, DecPair]
Decs2 = List[Decs]


def set_decimal_context() -> None:
    context: Context = Context(prec=32, rounding=ROUND_FLOOR)
    context.traps[FloatOperation] = True
    setcontext(context)
