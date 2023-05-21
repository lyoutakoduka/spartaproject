#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.json_context import Json
from scripts.files.export_json import json_dump


def is_same_json(left: Json, right: Json) -> bool:
    return 1 == len(list(set([
        json_dump(input, compress=True)
        for input in [left, right]
    ])))
