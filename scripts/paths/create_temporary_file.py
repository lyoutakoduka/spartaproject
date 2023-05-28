#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from scripts.files.jsons.export_json import json_export
from scripts.paths.create_directory_parent import create_directory_parent


def create_temporary_file(file_root: Path) -> Path:
    NAME: str = 'temporary'
    file_path: Path = Path(file_root, NAME + '.json')
    create_directory_parent(file_path)
    return json_export(file_path, NAME)
