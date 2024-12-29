#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to check that two Json objects are same."""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.file.json_context import Json
from pyspartalib.script.file.json.export_json import json_dump


def _convert_string(left: Json, right: Json) -> Strs:
    return [json_dump(source, compress=True) for source in [left, right]]


def is_same_json(left: Json, right: Json) -> bool:
    """Check that two Json objects are same.

    Args:
        left (Json): Json object used for comparing.

        right (Json): Json object used for comparing.

    Returns:
        bool: True if two Json objects are same.
    """
    return 1 == len(list(set(_convert_string(left, right))))
