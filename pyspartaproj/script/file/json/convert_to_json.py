#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import PurePath
from typing import Dict, List

from pyspartaproj.context.file.json_context import Json, Multi, Multi2, Single


def _convert_unknown(value: Single) -> Single:
    if isinstance(value, PurePath):
        return str(value)

    if isinstance(value, Decimal):
        return float(value)

    return value


def to_safe_json(value_json: Json) -> Json:
    if isinstance(value_json, Dict):
        return {key: to_safe_json(value) for key, value in value_json.items()}

    if isinstance(value_json, List):
        return [to_safe_json(value) for value in value_json]

    return _convert_unknown(value_json)


def multiple_to_json(value_json: Multi) -> Json:
    if isinstance(value_json, List):
        return [_convert_unknown(value) for value in value_json]

    return {key: _convert_unknown(value) for key, value in value_json.items()}


def multiple2_to_json(value_json: Multi2) -> Json:
    if isinstance(value_json, List):
        return [multiple_to_json(value) for value in value_json]

    return {key: multiple_to_json(value) for key, value in value_json.items()}
