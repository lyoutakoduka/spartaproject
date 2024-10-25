#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.json.export_json import json_dump


def _convert_string(left: Json, right: Json) -> Strs:
    return [json_dump(source, compress=True) for source in [left, right]]


def is_same_json(left: Json, right: Json) -> bool:
    return 1 == len(list(set(_convert_string(left, right))))
