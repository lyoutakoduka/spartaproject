#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict

from context.decimal_context import Decimal, Decs, Decs2, DecPair, DecPair2
from context.default.bool_context import Bools, Bools2, BoolPair, BoolPair2
from context.default.integer_context import Ints, Ints2, IntPair, IntPair2
from context.default.string_context import Strs, Strs2, StrPair, StrPair2
from context.json_context import Json, Single
from context.path_context import Path, Paths, Paths2, PathPair, PathPair2


def _convert_unknown(input: Single, key: str) -> Single:
    if isinstance(input, str):
        if 'path' in key:
            return Path(input)

    if isinstance(input, float):
        return Decimal(str(input))

    return input


def from_safe_json(input: Json, key: str = '') -> Json:
    if isinstance(input, Dict):
        return {
            key: from_safe_json(value, key=key)
            for key, value in input.items()
        }

    if isinstance(input, List):
        return [from_safe_json(value) for value in input]

    return _convert_unknown(input, key)


def _to_decimal(input: float) -> Decimal:
    return Decimal(str(input))


def _to_path(input: str) -> Path:
    return Path(input)


def bool_array_from_json(input: Json) -> Bools:
    if not isinstance(input, List):
        return []
    return [value for value in input if isinstance(value, bool)]


def integer_array_from_json(input: Json) -> Ints:
    if not isinstance(input, List):
        return []
    return [value for value in input if isinstance(value, int)]


def string_array_from_json(input: Json) -> Strs:
    if not isinstance(input, List):
        return []
    return [value for value in input if isinstance(value, str)]


def decimal_array_from_json(input: Json) -> Decs:
    if not isinstance(input, List):
        return []
    return [
        _to_decimal(value) for value in input if isinstance(value, float)
    ]


def path_array_from_json(input: Json) -> Paths:
    if not isinstance(input, List):
        return []
    return [_to_path(value) for value in input if isinstance(value, str)]


def bool_pair_from_json(input: Json) -> BoolPair:
    if not isinstance(input, Dict):
        return {}
    return {
        key: value for key, value in input.items() if isinstance(value, bool)
    }


def integer_pair_from_json(input: Json) -> IntPair:
    if not isinstance(input, Dict):
        return {}
    return {
        key: value for key, value in input.items() if isinstance(value, int)
    }


def string_pair_from_json(input: Json) -> StrPair:
    if not isinstance(input, Dict):
        return {}
    return {
        key: value for key, value in input.items() if isinstance(value, str)
    }


def decimal_pair_from_json(input: Json) -> DecPair:
    if not isinstance(input, Dict):
        return {}
    return {
        key: _to_decimal(value)
        for key, value in input.items()
        if isinstance(value, float)
    }


def path_pair_from_json(input: Json) -> PathPair:
    if not isinstance(input, Dict):
        return {}
    return {
        key: _to_path(value)
        for key, value in input.items()
        if isinstance(value, str)
    }


def bool_array2_from_json(input: Json) -> Bools2:
    if not isinstance(input, List):
        return []
    return [bool_array_from_json(value) for value in input]


def integer_array2_from_json(input: Json) -> Ints2:
    if not isinstance(input, List):
        return []
    return [integer_array_from_json(value) for value in input]


def string_array2_from_json(input: Json) -> Strs2:
    if not isinstance(input, List):
        return []
    return [string_array_from_json(value) for value in input]


def decimal_array2_from_json(input: Json) -> Decs2:
    if not isinstance(input, List):
        return []
    return [decimal_array_from_json(value) for value in input]


def path_array2_from_json(input: Json) -> Paths2:
    if not isinstance(input, List):
        return []
    return [path_array_from_json(value) for value in input]


def bool_pair2_from_json(input: Json) -> BoolPair2:
    if not isinstance(input, Dict):
        return {}
    return {
        key: bool_pair_from_json(value) for key, value in input.items()
    }


def integer_pair2_from_json(input: Json) -> IntPair2:
    if not isinstance(input, Dict):
        return {}
    return {
        key: integer_pair_from_json(value) for key, value in input.items()
    }


def string_pair2_from_json(input: Json) -> StrPair2:
    if not isinstance(input, Dict):
        return {}
    return {
        key: string_pair_from_json(value) for key, value in input.items()
    }


def decimal_pair2_from_json(input: Json) -> DecPair2:
    if not isinstance(input, Dict):
        return {}
    return {
        key: decimal_pair_from_json(value) for key, value in input.items()
    }


def path_pair2_from_json(input: Json) -> PathPair2:
    if not isinstance(input, Dict):
        return {}
    return {
        key: path_pair_from_json(value) for key, value in input.items()
    }
