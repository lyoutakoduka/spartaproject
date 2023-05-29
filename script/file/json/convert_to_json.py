#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

from context.json_context import Json, Single, Multi, Multi2


def _convert_unknown(input: Single) -> Single:
    if isinstance(input, Path):
        return str(input)

    if isinstance(input, Decimal):
        return float(input)

    return input


def to_safe_json(input: Json) -> Json:
    if isinstance(input, Dict):
        return {key: to_safe_json(value) for key, value in input.items()}

    if isinstance(input, List):
        return [to_safe_json(value) for value in input]

    return _convert_unknown(input)


def multiple_to_json(input: Multi) -> Json:
    if isinstance(input, List):
        return [_convert_unknown(value) for value in input]

    return {key: _convert_unknown(value) for key, value in input.items()}


def multiple2_to_json(input: Multi2) -> Json:
    if isinstance(input, List):
        return [multiple_to_json(value) for value in input]

    return {key: multiple_to_json(value) for key, value in input.items()}
