#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.extension.path_context import PathPair, Paths


def get_absolute(relative_path: Path, root_path: Path = Path()) -> Path:
    if relative_path.is_absolute():
        return relative_path

    if '.' == str(root_path):
        return relative_path.absolute()  # resolve() ignore symbolic link

    return Path(root_path, relative_path)


def get_absolute_array(relative_paths: Paths) -> Paths:
    return [get_absolute(path) for path in relative_paths]


def get_absolute_pair(relative_pair: PathPair) -> PathPair:
    return {key: get_absolute(path) for key, path in relative_pair.items()}
