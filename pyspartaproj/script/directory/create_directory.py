#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.extension.path_context import PathPair, Paths


def create_directory(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_directory_array(paths: Paths) -> Paths:
    return [create_directory(path) for path in paths]


def create_directory_pair(path_pair: PathPair) -> PathPair:
    return {key: create_directory(path) for key, path in path_pair.items()}
