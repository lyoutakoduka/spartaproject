#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.path_context import Path, Paths, PathPair


def path_mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def path_array_mkdir(paths: Paths) -> None:
    for path in paths:
        path_mkdir(path)


def path_pair_mkdir(path_pair: PathPair) -> None:
    for _, path in path_pair.items():
        path_mkdir(path)
