#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from json import loads
from pathlib import Path
from typing import List, Dict

from contexts.json_context import Json, Single
from scripts.files.import_file import text_import


def _convert_unknown(input: Single, key: str) -> Single:
    if isinstance(input, str):
        if 0 < len(key):
            if 'path' in key:
                return Path(input)

    if isinstance(input, float):
        return Decimal(str(input))

    return input


def _deserialize_json(input: Json, key: str = '') -> Json:
    if isinstance(input, Dict):
        return {
            key: _deserialize_json(value, key=key)
            for key, value in input.items()
        }

    if isinstance(input, List):
        return [_deserialize_json(value) for value in input]

    return _convert_unknown(input, key)


def json_load(input: str) -> Json:
    return _deserialize_json(loads(input))


def json_import(import_path: Path) -> Json:
    return json_load(text_import(import_path))
