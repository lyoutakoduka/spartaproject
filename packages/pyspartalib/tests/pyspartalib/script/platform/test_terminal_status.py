#!/usr/bin/env python

from os import getenv

from pyspartalib.context.custom.type_context import Type


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _get_environment(key: str) -> str:
    return _none_error(getenv(key.upper()))
