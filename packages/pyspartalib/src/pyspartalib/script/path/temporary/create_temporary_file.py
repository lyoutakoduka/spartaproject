#!/usr/bin/env python

"""Module to create empty temporary file as json format."""

from pathlib import Path

from pyspartalib.script.directory.create_parent import create_parent
from pyspartalib.script.file.json.export_json import json_export


def create_temporary_file(
    file_root: Path,
    file_name: str | None = None,
) -> Path:
    """Create empty temporary file as json format.

    Args:
        file_root (Path):
            Path of directory which empty temporary file is created.

        file_name (str | None, optional): Defaults to None.
            Name of created file which is json format.

    Returns:
        Path: Path of created empty temporary file.

    """
    if file_name is None:
        file_name = "temporary"

    file_path: Path = Path(file_root, file_name + ".json")
    create_parent(file_path)
    return json_export(file_path, "empty")
