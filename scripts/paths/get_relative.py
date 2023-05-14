#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.path_context import Path, Paths, PathPair


def path_relative(absolute_path: Path, root_path: Path = Path()) -> Path:
    if '.' == str(root_path):
        root_path = Path.cwd()

    return absolute_path.relative_to(root_path)


def path_array_relative(absolute_paths: Paths, root_path: Path = Path()) -> Paths:
    return [path_relative(path, root_path=root_path) for path in absolute_paths]


def path_pair_relative(absolute_pair: PathPair, root_path: Path = Path()) -> PathPair:
    return {key: path_relative(path, root_path=root_path) for key, path in absolute_pair.items()}
