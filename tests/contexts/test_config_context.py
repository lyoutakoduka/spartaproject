#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Any, get_args
from decimal import Decimal
from pathlib import Path

from contexts.config_context import Config, ConfigExtend


def _check_type_structure(check_type: type) -> bool:
    is_extend: bool = ConfigExtend == check_type

    section_key, section = get_args(check_type)

    if section_key != str:
        return False

    default_types: List[type] = [bool, int, float, str]
    default_type_union = bool | int | float | str

    if is_extend:
        default_types += [Decimal, Path]
        default_type_union |= Decimal | Path

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


def test_extend() -> None:
    assert _check_type_structure(ConfigExtend)


def main() -> bool:
    test_type()
    test_extend()
    return True
