#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.directory.create_directory import create_directory


def create_directory_parent(child_path: Path) -> Path:
    path: Path = child_path.parent
    if path.exists():
        return path
    return create_directory(path)
