#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.path_context import Path, Paths, PathPair


def _default() -> Path:
    return Path.cwd()


def path_relative(absolute_path: Path, root_path: Path = _default()) -> Path:
    return absolute_path.relative_to(root_path)


def path_array_relative(absolute_paths: Paths, root_path: Path = _default()) -> Paths:
    return [path_relative(path, root_path) for path in absolute_paths]


def path_pair_relative(absolute_pair: PathPair, root_path: Path = _default()) -> PathPair:
    return {key: path_relative(path, root_path) for key, path in absolute_pair.items()}
