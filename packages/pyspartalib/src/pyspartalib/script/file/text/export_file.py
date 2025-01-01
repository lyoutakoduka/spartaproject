#!/usr/bin/env python

"""Module to export text file."""

from pathlib import Path

from pyspartalib.script.string.encoding.set_encoding import set_encoding


def _unix_line_brake(text: str) -> str:
    return text.replace("\r\n", "\n")


def byte_export(export_path: Path, source: bytes) -> Path:
    """Export binary file.

    Args:
        export_path (Path): Path which is used for exporting data.

        source (bytes): Binary data you want to export.

    Returns:
        Path: Path of data which is finally exported.

    """
    with export_path.open("wb") as file:
        file.write(source)

    return export_path


def text_export(
    export_path: Path, source: str, encoding: str | None = None
) -> Path:
    """Export text file.

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
        set_encoding(_unix_line_brake(source), encoding=encoding),
    )
