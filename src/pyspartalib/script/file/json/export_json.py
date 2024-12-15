#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to export data used for json format."""

from json import dumps
from pathlib import Path

from pyspartalib.context.default.string_context import StrTuple
from pyspartalib.context.file.json_context import Json
from pyspartalib.script.file.text.export_file import text_export


def json_dump(source: Json, compress: bool = False) -> str:
    """Function to convert data used for json format.

    Return following triple quoted text if argument "source" is...

    {"bool": True, "int": 1, "str": "1"}

    '''
      {
        "bool": true,
        "int": 1,
        "str": "1"
      }
    '''

    Args:
        source (Json): Data used for json format you want to convert.

        compress (bool, optional): Defaults to False.
            Return following single quoted text if argument "compress" is True.

            '{"bool":true,"int":1,"str":"1"}'

    Returns:
        str: Converted text used for json format.
    """
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
    """Function to export data used for json format.

    Args:
        export_path (Path): Path which is used for exporting data.

        source (Json): Data used for json format you want to export.

        compress (bool, optional): Defaults to False.
            True if you want to export small and obfuscated text.
            It's used for argument "compress" of function "json_dump".

    Returns:
        Path: Path of data which is finally exported.
    """
    return text_export(export_path, json_dump(source, compress=compress))
