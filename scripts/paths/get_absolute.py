#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.path_context import Path, Paths, PathPair


def get_absolute(relative_path: Path) -> Path:
    return relative_path.absolute()  # resolve() ignore symbolic link


def get_absolute_array(relative_paths: Paths) -> Paths:
    return [get_absolute(path) for path in relative_paths]


def get_absolute_pair(relative_pair: PathPair) -> PathPair:
    return {key: get_absolute(path) for key, path in relative_pair.items()}
