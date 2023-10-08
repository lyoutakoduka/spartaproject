#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.script.path.modify.get_current import get_current


def get_absolute(relative_path: Path, root_path: Path | None = None) -> Path:
    if relative_path.is_absolute():
        return relative_path

    if root_path is None:
        root_path = get_current()

    return Path(root_path, relative_path)


def get_absolute_array(relative_paths: Paths) -> Paths:
    return [get_absolute(path) for path in relative_paths]


def get_absolute_pair(relative_pair: PathPair) -> PathPair:
    return {key: get_absolute(path) for key, path in relative_pair.items()}
