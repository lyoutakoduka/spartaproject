#!/usr/bin/env python

from pathlib import Path

from pyspartalib.context.custom.type_context import Type


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_current() -> Path:
    return Path().cwd()
