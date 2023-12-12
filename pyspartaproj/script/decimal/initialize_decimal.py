#!/usr/bin/env python
# -*- coding: utf-8 -*-


from decimal import ROUND_FLOOR, Context, FloatOperation, setcontext


def initialize_decimal() -> None:
    context: Context = Context(prec=32, rounding=ROUND_FLOOR)
    context.traps[FloatOperation] = True
    setcontext(context)
