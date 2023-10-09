#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    if isinstance(value_json, Dict):
        return {
            key: from_safe_json(value, key=key)
            for key, value in value_json.items()
        }

    if isinstance(value_json, List):
        return [from_safe_json(value) for value in value_json]

    return _convert_unknown(value_json, key)


def bool_array_from_json(value_json: Json) -> Bools:
    if not isinstance(value_json, List):
        return []
    return [value for value in value_json if isinstance(value, bool)]


def integer_array_from_json(value_json: Json) -> Ints:
    if not isinstance(value_json, List):
        return []
    return [value for value in value_json if isinstance(value, int)]


def string_array_from_json(value_json: Json) -> Strs:
    if not isinstance(value_json, List):
        return []
    return [value for value in value_json if isinstance(value, str)]


def decimal_array_from_json(value_json: Json) -> Decs:
    if not isinstance(value_json, List):
        return []
    return [
        _to_decimal(value) for value in value_json if isinstance(value, float)
    ]


def path_array_from_json(value_json: Json) -> Paths:
    if not isinstance(value_json, List):
        return []
    return [_to_path(value) for value in value_json if isinstance(value, str)]


def bool_pair_from_json(value_json: Json) -> BoolPair:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, bool)
    }


def integer_pair_from_json(value_json: Json) -> IntPair:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, int)
    }


def string_pair_from_json(value_json: Json) -> StrPair:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, str) and not _filter_path(value, key)
    }


def decimal_pair_from_json(value_json: Json) -> DecPair:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: _to_decimal(value)
        for key, value in value_json.items()
        if isinstance(value, float)
    }


def path_pair_from_json(value_json: Json) -> PathPair:
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
    if not isinstance(value_json, List):
        return []
    return [bool_array_from_json(value) for value in value_json]


def integer_array2_from_json(value_json: Json) -> Ints2:
    if not isinstance(value_json, List):
        return []
    return [integer_array_from_json(value) for value in value_json]


def string_array2_from_json(value_json: Json) -> Strs2:
    if not isinstance(value_json, List):
        return []
    return [string_array_from_json(value) for value in value_json]


def decimal_array2_from_json(value_json: Json) -> Decs2:
    if not isinstance(value_json, List):
        return []
    return [decimal_array_from_json(value) for value in value_json]


def path_array2_from_json(value_json: Json) -> Paths2:
    if not isinstance(value_json, List):
        return []
    return [path_array_from_json(value) for value in value_json]


def bool_pair2_from_json(value_json: Json) -> BoolPair2:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: bool_pair_from_json(value) for key, value in value_json.items()
    }


def integer_pair2_from_json(value_json: Json) -> IntPair2:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: integer_pair_from_json(value) for key, value in value_json.items()
    }


def string_pair2_from_json(value_json: Json) -> StrPair2:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: string_pair_from_json(value) for key, value in value_json.items()
    }


def decimal_pair2_from_json(value_json: Json) -> DecPair2:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: decimal_pair_from_json(value) for key, value in value_json.items()
    }


def path_pair2_from_json(value_json: Json) -> PathPair2:
    if not isinstance(value_json, Dict):
        return {}
    return {
        key: path_pair_from_json(value) for key, value in value_json.items()
    }
