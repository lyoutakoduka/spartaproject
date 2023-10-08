#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.directory.create_directory_parent import (
    create_directory_parent,
)
from pyspartaproj.script.file.json.export_json import json_export


def create_temporary_file(file_root: Path) -> Path:
    name: str = "temporary"
    file_path: Path = Path(file_root, name + ".json")
    create_directory_parent(file_path)
    return json_export(file_path, name)
