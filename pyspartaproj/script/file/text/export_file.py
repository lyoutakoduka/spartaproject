#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to export text file."""

from pathlib import Path


def byte_export(export_path: Path, source: bytes) -> Path:
    """Function to export binary file.

    Args:
        export_path (Path): Path which is used for exporting data.

        source (bytes): Binary data you want to export.

    Returns:
        Path: Path of data which is finally exported.
    """
    with open(export_path, "wb") as file:
        file.write(source)

    return export_path


def set_encoding(source: str, encoding: str | None = None) -> bytes:
    """Encode string by specific character encoding.

    Args:
        source (str): String data you want to encode.

        encoding (str | None, optional): Defaults to None.
            Character encoding you want to override forcibly.
            Default character encoding is "utf-8".

    Returns:
        bytes: Converted Byte date.
    """
    if encoding is None:
        encoding = "utf-8"

    return source.encode(encoding)


def text_export(
    export_path: Path, source: str, encoding: str | None = None
) -> Path:
    """Function to export text file.

    Args:
        export_path (Path): Path which is used for exporting data.

        source (str): String data you want to export.

        encoding (str | None, optional): Defaults to None.
            Character encoding you want to override forcibly.
            It's used for argument "encoding" of function "set_encoding".

    Returns:
        Path: Path of data which is finally exported.
    """
    if encoding is None:
        encoding = "utf-8"

    return byte_export(
        export_path,
        set_encoding(source.replace("\r\n", "\n"), encoding=encoding),
    )
