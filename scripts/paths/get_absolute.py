#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.path_context import Path, Paths, PathPair


def path_absolute(relative_path: Path) -> Path:
    return relative_path.absolute()  # resolve() ignore symbolic link


def path_array_absolute(relative_paths: Paths) -> Paths:
    return [path_absolute(path) for path in relative_paths]


def path_pair_absolute(relative_pair: PathPair) -> PathPair:
    return {key: path_absolute(path) for key, path in relative_pair.items()}
