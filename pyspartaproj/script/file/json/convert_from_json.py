#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert data from json format."""

from decimal import Decimal
from pathlib import Path
from typing import Dict, List

from pyspartaproj.context.default.bool_context import (
    BoolPair,
    BoolPair2,
    Bools,
    Bools2,
)
from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints,
    Ints2,
)
from pyspartaproj.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartaproj.context.extension.decimal_context import (
    DecPair,
    DecPair2,
    Decs,
    Decs2,
)
from pyspartaproj.context.extension.path_context import (
    PathPair,
    PathPair2,
    Paths,
    Paths2,
)
from pyspartaproj.context.file.json_context import Json, Single


def _to_decimal(number: float) -> Decimal:
    return Decimal(str(number))


def _to_path(text: str) -> Path:
    return Path(text)


def _filter_path(text: str, key: str) -> Path | None:
    if key.endswith(".path"):
        return _to_path(text)

    return None


def _convert_unknown(value: Single, key: str | None) -> Single:
    if isinstance(value, float):
        return _to_decimal(value)

    if isinstance(value, str):
        if key is not None:
            if path := _filter_path(value, key):
                return path

    return value


def from_safe_json(value_json: Json, key: str | None = None) -> Json:
    """Convert default json format data to custom json format.

    Difference between custom json format and default are following 2 point.

    1. Custom json format treat type "float" of default as type "Decimal".

    2. Custom json format treat type "str" of default as type "Path".
        if the key of value end with text ".path".

    In this function, type "float" and "str" are
        automatically converted as noted above.

    Args:
        value_json (Json): Default json format data you want to convert.

        key (str | None, optional):
            String key used for converting type "Path" value.

    Returns:
        Json: Converted data which is custom json format.
    """
    if isinstance(value_json, Dict):
        return {
            key: from_safe_json(value, key=key)
            for key, value in value_json.items()
        }

    if isinstance(value_json, List):
        return [from_safe_json(value) for value in value_json]

    return _convert_unknown(value_json, key)


def bool_array_from_json(value_json: Json) -> Bools:
    """Convert json format data to list of type "bool".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Bools: Converted data which is list of type "bool".
    """
    if not isinstance(value_json, List):
        return []

    return [value for value in value_json if isinstance(value, bool)]


def integer_array_from_json(value_json: Json) -> Ints:
    """Convert json format data to list of type "int".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Ints: Converted data which is list of type "int".
    """
    if not isinstance(value_json, List):
        return []

    return [value for value in value_json if isinstance(value, int)]


def string_array_from_json(value_json: Json) -> Strs:
    """Convert json format data to list of type "str".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Strs: Converted data which is list of type "str".
    """
    if not isinstance(value_json, List):
        return []

    return [value for value in value_json if isinstance(value, str)]


def decimal_array_from_json(value_json: Json) -> Decs:
    """Convert json format data to list of type "Decimal".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Decs: Converted data which is list of type "Decimal".
    """
    if not isinstance(value_json, List):
        return []

    return [
        _to_decimal(value) for value in value_json if isinstance(value, float)
    ]


def path_array_from_json(value_json: Json) -> Paths:
    """Convert json format data to list of type "Path".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Paths: Converted data which is list of type "Path".
    """
    if not isinstance(value_json, List):
        return []

    return [_to_path(value) for value in value_json if isinstance(value, str)]


def bool_pair_from_json(value_json: Json) -> BoolPair:
    """Convert json format data to dictionary of type "bool".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        BoolPair: Converted data which is dictionary of type "bool".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, bool)
    }


def integer_pair_from_json(value_json: Json) -> IntPair:
    """Convert json format data to dictionary of type "int".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        IntPair: Converted data which is dictionary of type "int".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, int)
    }


def string_pair_from_json(value_json: Json) -> StrPair:
    """Convert json format data to dictionary of type "str".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        StrPair: Converted data which is dictionary of type "str".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, str) and not _filter_path(value, key)
    }


def decimal_pair_from_json(value_json: Json) -> DecPair:
    """Convert json format data to dictionary of type "Decimal".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        DecPair: Converted data which is dictionary of type "Decimal".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: _to_decimal(value)
        for key, value in value_json.items()
        if isinstance(value, float)
    }


def path_pair_from_json(value_json: Json) -> PathPair:
    """Convert json format data to dictionary of type "Path".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        PathPair: Converted data which is dictionary of type "Path".
    """
    if not isinstance(value_json, Dict):
        return {}

    paths: PathPair = {}

    for key, value in value_json.items():
        if not isinstance(value, str):
            continue

        if path := _filter_path(value, key):
            paths[key] = path

    return paths


def bool_array2_from_json(value_json: Json) -> Bools2:
    """Convert json format data to 2 dimensional list of type "bool".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Bools2: Converted data which is 2 dimensional list of type "bool".
    """
    if not isinstance(value_json, List):
        return []

    return [bool_array_from_json(value) for value in value_json]


def integer_array2_from_json(value_json: Json) -> Ints2:
    """Convert json format data to 2 dimensional list of type "int".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Ints2: Converted data which is 2 dimensional list of type "int".
    """
    if not isinstance(value_json, List):
        return []

    return [integer_array_from_json(value) for value in value_json]


def string_array2_from_json(value_json: Json) -> Strs2:
    """Convert json format data to 2 dimensional list of type "str".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Strs2: Converted data which is 2 dimensional list of type "str".
    """
    if not isinstance(value_json, List):
        return []

    return [string_array_from_json(value) for value in value_json]


def decimal_array2_from_json(value_json: Json) -> Decs2:
    """Convert json format data to 2 dimensional list of type "Decimal".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Decs2: Converted data which is 2 dimensional list of type "Decimal".
    """
    if not isinstance(value_json, List):
        return []

    return [decimal_array_from_json(value) for value in value_json]


def path_array2_from_json(value_json: Json) -> Paths2:
    """Convert json format data to 2 dimensional list of type "Path".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        Paths2: Converted data which is 2 dimensional list of type "Path".
    """
    if not isinstance(value_json, List):
        return []

    return [path_array_from_json(value) for value in value_json]


def bool_pair2_from_json(value_json: Json) -> BoolPair2:
    """Convert json format data to 2 dimensional dictionary of type "bool".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        BoolPair2:
            Converted data which is 2 dimensional dictionary of type "bool".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: bool_pair_from_json(value) for key, value in value_json.items()
    }


def integer_pair2_from_json(value_json: Json) -> IntPair2:
    """Convert json format data to 2 dimensional dictionary of type "int".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        IntPair2:
            Converted data which is 2 dimensional dictionary of type "int".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: integer_pair_from_json(value) for key, value in value_json.items()
    }


def string_pair2_from_json(value_json: Json) -> StrPair2:
    """Convert json format data to 2 dimensional dictionary of type "str".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        StrPair2:
            Converted data which is 2 dimensional dictionary of type "str".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: string_pair_from_json(value) for key, value in value_json.items()
    }


def decimal_pair2_from_json(value_json: Json) -> DecPair2:
    """Convert json format data to 2 dimensional dictionary of type "Decimal".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        DecPair2:
            Converted data which is 2 dimensional dictionary of type "Decimal".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: decimal_pair_from_json(value) for key, value in value_json.items()
    }


def path_pair2_from_json(value_json: Json) -> PathPair2:
    """Convert json format data to 2 dimensional dictionary of type "Path".

    Args:
        value_json (Json): Json format data you want to convert.

    Returns:
        PathPair2:
            Converted data which is 2 dimensional dictionary of type "Path".
    """
    if not isinstance(value_json, Dict):
        return {}

    return {
        key: path_pair_from_json(value) for key, value in value_json.items()
    }
