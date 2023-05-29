#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.file.json_context import Json
from script.file.json.export_json import json_dump


def is_same_json(left: Json, right: Json) -> bool:
    return 1 == len(list(set([
        json_dump(input, compress=True) for input in [left, right]
    ])))
