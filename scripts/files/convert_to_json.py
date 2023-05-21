#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

from contexts.json_context import Json, Single, Array, Array2, Pair, Pair2


def _convert_unknown(input: Single) -> Single:
    if isinstance(input, Path):
        return str(input)

    if isinstance(input, Decimal):
        return float(input)

    return input


def to_safe_json(content: Json) -> Json:
    if isinstance(content, Dict):
        return {key: to_safe_json(value) for key, value in content.items()}

    if isinstance(content, List):
        return [to_safe_json(value) for value in content]

    return _convert_unknown(content)


def array_to_json(input: Array) -> Json:
    return [_convert_unknown(value) for value in input]


def array2_to_json(input: Array2) -> Json:
    return [array_to_json(value) for value in input]


def pair_to_json(input: Pair) -> Json:
    return {key: _convert_unknown(value) for key, value in input.items()}


def pair2_to_json(input: Pair2) -> Json:
    return {key: pair_to_json(value) for key, value in input.items()}
