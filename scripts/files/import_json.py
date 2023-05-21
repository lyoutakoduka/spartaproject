#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from json import loads
from pathlib import Path
from typing import List, Dict

from contexts.json_context import Json, Single
from scripts.files.import_file import text_import


def _convert_unknown(content: Single, key: str) -> Single:
    if isinstance(content, str):
        if 0 < len(key):
            if 'path' in key:
                return Path(content)

    if isinstance(content, float):
        return Decimal(str(content))

    return content


def _deserialize_json(content: Json, key: str = '') -> Json:
    if isinstance(content, Dict):
        return {
            key: _deserialize_json(value, key=key)
            for key, value in content.items()
        }

    if isinstance(content, List):
        return [_deserialize_json(value) for value in content]

    return _convert_unknown(content, key)


def json_load(content: str) -> Json:
    return _deserialize_json(loads(content))


def json_import(import_path: Path) -> Json:
    return json_load(text_import(import_path))
