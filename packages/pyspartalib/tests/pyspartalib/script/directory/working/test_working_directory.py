#!/usr/bin/env python

from pyspartalib.context.custom.type_context import Type


def _difference_error(result: Type, expected: Type) -> None:
    if expected != result:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError
