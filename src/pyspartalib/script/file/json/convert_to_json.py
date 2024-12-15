#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert data to json format."""

from decimal import Decimal
from pathlib import PurePath
from typing import Dict, List

from pyspartalib.context.file.json_context import Json, Multi, Multi2, Single


def _convert_unknown(value: Single) -> Single:
    if isinstance(value, PurePath):
        return str(value)

    if isinstance(value, Decimal):
        return float(value)

    return value


def to_safe_json(value_json: Json) -> Json:
    """Convert custom json format data to default json format.

    Difference between custom json format and default are following 2 point.

    1. Custom json format treat type "float" of default as type "Decimal".

    2. Custom json format treat type "str" of default as type "Path".
        if the key of value end with text ".path".

    In this function, type "Decimal" and "Path" are
        automatically converted to default types as noted above.

    Args:
        value_json (Json): Custom json format data you want to convert.

    Returns:
        Json: Converted data which is default json format.
    """
    if isinstance(value_json, Dict):
        return {key: to_safe_json(value) for key, value in value_json.items()}

    if isinstance(value_json, List):
        return [to_safe_json(value) for value in value_json]

    return _convert_unknown(value_json)


def multiple_to_json(value_json: Multi) -> Json:
    """Convert data which is type list or dictionary to json format.

    Args:
        value_json (Multi): List or dictionary data you want to convert.
            Type "Multi" only allow following types of list or dictionary.

            [bool, int, float, Decimal, str, Path]

    Returns:
        Json: Converted data which is json format.
    """
    if isinstance(value_json, List):
        return [_convert_unknown(value) for value in value_json]

    return {key: _convert_unknown(value) for key, value in value_json.items()}


def multiple2_to_json(value_json: Multi2) -> Json:
    """Convert data which is 2 dimensional list or dictionary to json format.

    Args:
        value_json (Multi2):
            2 dimensional list or dictionary you want to convert.

    Returns:
        Json: Converted data which is json format.
    """
    if isinstance(value_json, List):
        return [multiple_to_json(value) for value in value_json]

    return {key: multiple_to_json(value) for key, value in value_json.items()}
