#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.path_context import Path, Paths, PathPair


def path_mkdir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def path_array_mkdir(paths: Paths) -> Paths:
    return [path_mkdir(path) for path in paths]


def path_pair_mkdir(path_pair: PathPair) -> PathPair:
    return {key: path_mkdir(path) for key, path in path_pair.items()}
