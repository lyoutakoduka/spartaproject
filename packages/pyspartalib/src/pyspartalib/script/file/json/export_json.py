#!/usr/bin/env python

"""Module to export data used for json format."""

from json import dumps
from pathlib import Path

from pyspartalib.context.default.string_context import StrTuple
from pyspartalib.context.file.json_context import Json
from pyspartalib.script.file.text.export_file import text_export


def _get_separators(compress: bool) -> StrTuple | None:
    return (",", ":") if compress else None


def _get_indent(compress: bool) -> int | None:
    return None if compress else 2


def json_dump(source: Json, compress: bool = False) -> str:
    """Convert data used for json format.

    When argument "source" is follow.

        {"bool": True, "int": 1, "str": "1"}

    Return following text.

        {
            "bool": true,
            "int": 1,
            "str": "1"
        }

    Args:
        source (Json): Data used for json format you want to convert.

        compress (bool, optional): Defaults to False.
            Return following single quoted text if argument "compress" is True.

                {"bool":true,"int":1,"str":"1"}

    Returns:
        str: Converted text used for json format.

    """
    return dumps(
        source,
        ensure_ascii=False,
        sort_keys=True,
        indent=_get_indent(compress),
        separators=_get_separators(compress),
    )


def json_export(
    export_path: Path,
    source: Json,
    compress: bool = False,
) -> Path:
    """Export data used for json format.

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
