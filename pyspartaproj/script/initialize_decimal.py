#!/usr/bin/env python
# -*- coding: utf-8 -*-


from decimal import ROUND_FLOOR, Context, FloatOperation, setcontext


def set_decimal_context() -> None:
    context: Context = Context(prec=32, rounding=ROUND_FLOOR)
    context.traps[FloatOperation] = True
    setcontext(context)
