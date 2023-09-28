#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from pathlib import Path

from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.text.import_file import text_import


def json_load(input: str) -> Json:
    result: Json = loads(input)
    return result


def json_import(import_path: Path) -> Json:
    return json_load(text_import(import_path))
