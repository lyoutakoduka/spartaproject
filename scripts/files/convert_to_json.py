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


def get_safe_json(content: Json) -> Json:
    if isinstance(content, Dict):
        return {key: get_safe_json(value) for key, value in content.items()}

    if isinstance(content, List):
        return [get_safe_json(value) for value in content]

    return _convert_unknown(content)


def json_from_pair(input: Pair) -> Json:
    return {key: _convert_unknown(value) for key, value in input.items()}


def json_from_pair2(input: Pair2) -> Json:
    return {key: json_from_pair(value) for key, value in input.items()}


def json_from_array(input: Array) -> Json:
    return [_convert_unknown(value) for value in input]


def json_from_array2(input: Array2) -> Json:
    return [json_from_array(value) for value in input]
