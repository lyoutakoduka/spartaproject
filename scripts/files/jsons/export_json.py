#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps
from pathlib import Path

from context.defaults.string_context import StrTuple
from context.json_context import Json
from scripts.files.export_file import text_export


def json_dump(input: Json, compress: bool = False) -> str:
    separators: StrTuple | None = (',', ':') if compress else None
    indent: int | None = None if compress else 2

    return dumps(
        input,
        ensure_ascii=False,
        sort_keys=True,
        indent=indent,
        separators=separators,
    )


def json_export(
    export_path: Path, input: Json, compress: bool = False,
) -> Path:
    return text_export(export_path, json_dump(input, compress=compress))
