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


def text_export(export_path: Path, source: str) -> Path:
    """Function to export text file.

    Args:
        export_path (Path): Path which is used for exporting data.

        source (str): Text data you want to export.

    Returns:
        Path: Path of data which is finally exported.
    """
    replaced = source.replace("\r\n", "\n")
    return byte_export(export_path, replaced.encode("utf-8"))
