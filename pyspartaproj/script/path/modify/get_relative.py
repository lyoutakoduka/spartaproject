#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from spartaproject.context.extension.path_context import PathPair, Paths


def get_relative(absolute_path: Path, root_path: Path = Path()) -> Path:
    if '.' == str(root_path):
        root_path = Path.cwd()

    if not absolute_path.is_relative_to(root_path):
        raise ValueError

    return absolute_path.relative_to(root_path)


def get_relative_array(
    absolute_paths: Paths, root_path: Path = Path()
) -> Paths:
    return [
        get_relative(path, root_path=root_path)
        for path in absolute_paths
    ]


def get_relative_pair(
    absolute_pair: PathPair, root_path: Path = Path()
) -> PathPair:
    return {
        key: get_relative(path, root_path=root_path)
        for key, path in absolute_pair.items()
    }
