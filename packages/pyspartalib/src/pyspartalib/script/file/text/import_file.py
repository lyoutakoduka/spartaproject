#!/usr/bin/env python

"""Module to import text file."""

from pathlib import Path

from pyspartalib.script.string.encoding.set_decoding import set_decoding


def _unix_line_brake(text: str) -> str:
    return text.replace("\r\n", "\n")


def byte_import(import_path: Path) -> bytes:
    """Import binary file.

    Args:
        import_path (Path): Path of binary file you want to import.

    Returns:
        bytes: Imported data from binary file.

    """
    with open(import_path, "rb") as file:
        return file.read()


def text_import(import_path: Path, encoding: str | None = None) -> str:
    """Import text file.

    Args:
        import_path (Path): Path of text file you want to import.

        encoding (str | None, optional): Defaults to None.
            Character encoding you want to override forcibly.

    Returns:
        str: Imported string from text file.

    """
    return _unix_line_brake(
        set_decoding(byte_import(import_path), encoding=encoding),
    )
