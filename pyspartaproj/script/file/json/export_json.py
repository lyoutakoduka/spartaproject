#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps
from pathlib import Path

from pyspartaproj.context.default.string_context import StrTuple
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.text.export_file import text_export


def json_dump(source: Json, compress: bool = False) -> str:
    separators: StrTuple | None = (",", ":") if compress else None
    indent: int | None = None if compress else 2

    return dumps(
        source,
        ensure_ascii=False,
        sort_keys=True,
        indent=indent,
        separators=separators,
    )


def json_export(
    export_path: Path, source: Json, compress: bool = False
) -> Path:
    return text_export(export_path, json_dump(source, compress=compress))
