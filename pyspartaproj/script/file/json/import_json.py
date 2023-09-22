#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from pathlib import Path

from spartaproject.context.file.json_context import Json
from spartaproject.script.file.text.import_file import text_import


def json_load(input: str) -> Json:
    return loads(input)


def json_import(import_path: Path) -> Json:
    return json_load(text_import(import_path))
