#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Any, get_args

from contexts.config_context import Config


def _check_type_structure(check_type: type) -> bool:
    section_key, section = get_args(check_type)

    if section_key != str:
        return False

    default_types: List[type] = [bool, int, float, str, Decimal, Path]
    default_type_union = bool | int | float | str | Decimal | Path

    expected_types: List[Any] = default_types + [default_type_union]

    items = get_args(section)

    for expected_type, options in zip(expected_types, items):
        option_key, option = get_args(options)

        if option_key != str:
            return False

        if option != expected_type:
            return False

    return True


def test_type() -> None:
    assert _check_type_structure(Config)


def main() -> bool:
    test_type()
    return True
