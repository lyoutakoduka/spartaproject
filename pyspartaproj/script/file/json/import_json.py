#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to import Json file or load Json data."""

from json import loads
from pathlib import Path

from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.text.import_file import text_import


def json_load(source: str) -> Json:
    """Load Json data from imported file.

    Supported data types of configuration file are follow.

    1: None
    2: Boolean
    3: Integer
    4: Decimal (Type float is always loaded as type decimal)
    5-1: String
    5-2: Path (If key of configuration data ends with string ".path")

    Args:
        source (str): Json data as string format.

    Returns:
        Json: Json data converted to user defined type.
    """
    result: Json = loads(source)
    return result


def json_import(import_path: Path, encoding: str | None = None) -> Json:
    """Import Json file as format "json".

    Args:
        import_path (Path): Path of Json file you want to import.

        encoding (str | None, optional): Defaults to None.
            Character encoding you want to override forcibly.
            It's used for argument "encoding" of function "text_import".

    Returns:
        Json: Json data converted to user defined type.
    """
    return json_load(text_import(import_path, encoding=encoding))
