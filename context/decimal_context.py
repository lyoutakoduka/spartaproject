#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import setcontext, Context, ROUND_FLOOR, FloatOperation, Decimal
from typing import List, Dict

DecPair = Dict[str, Decimal]
Decs = List[Decimal]

DecPair2 = Dict[str, DecPair]
Decs2 = List[Decs]


def set_decimal_context() -> None:
    context: Context = Context(prec=32, rounding=ROUND_FLOOR)
    context.traps[FloatOperation] = True
    setcontext(context)
