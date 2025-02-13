#!/usr/bin/env python

from pyspartalib.context.custom.type_context import Type


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _status_error(status: bool) -> None:
    if not status:
        raise ValueError
