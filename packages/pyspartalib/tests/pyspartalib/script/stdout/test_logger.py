#!/usr/bin/env python

from pyspartalib.context.callable_context import Type
from pyspartalib.script.stdout.logger import show_log


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected() -> str:
    return "test"


def _show_log() -> None:
    show_log(_get_expected())
