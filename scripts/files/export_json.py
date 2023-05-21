#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps
from pathlib import Path

from contexts.json_context import Json
from contexts.string_context import StrTuple
from scripts.files.export_file import text_export


def json_dump(content: Json, compress: bool = False) -> str:
    separators: StrTuple | None = (',', ':') if compress else None
    indent: int | None = None if compress else 2

    return dumps(
        content,
        ensure_ascii=False,
        sort_keys=True,
        indent=indent,
        separators=separators,
    )


def json_export(
    export_path: Path, content: Json, compress: bool = False,
) -> Path:
    return text_export(export_path, json_dump(content, compress=compress))
