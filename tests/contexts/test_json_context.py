#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Any, ForwardRef, get_args
from decimal import Decimal
from pathlib import Path

from contexts.json_context import Json, JsonSafe


def _check_type_structure(check_type: Any) -> bool:
    is_extend: bool = Json == check_type

    expected_types: List[type] = [
        type(None), bool, int, float, str, Decimal, Path]

    if is_extend:
        expected_types += [Decimal, Path]

    items = get_args(check_type)
    index: int = len(expected_types) - 2

    for expected_type, value in zip(expected_types, items[:index]):
        if expected_type != value:
            return False

    dict_type = get_args(items[-2])
    list_type = get_args(items[-1])

    if str != dict_type[0]:
        return False

    type_text: str = 'Json' if is_extend else 'JsonSafe'
    recursive = ForwardRef(type_text)

    for type_recursive in [dict_type[-1], list_type[0]]:
        if recursive != type_recursive:
            return False

    return True


def test_safe() -> None:
    assert _check_type_structure(JsonSafe)


def test_type() -> None:
    assert _check_type_structure(Json)


def main() -> bool:
    test_safe()
    test_type()
    return True
