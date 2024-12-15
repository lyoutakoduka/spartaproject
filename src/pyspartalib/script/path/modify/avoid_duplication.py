#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert path to avoid existing path."""

from pathlib import Path


def get_avoid_path(path: Path) -> Path:
    """Function to convert path to avoid existing path.

    Converting process and that condition is follow.

    root/
        |--before.txt
        |--after.txt

    Think that renaming "before.txt" to "after.txt", first.
    You can use the function like here.

    source: Path = "root/after.txt"
    destination: Path = get_avoid_path(source)
    rename(source, destination)

    Contents of directory tree after renaming is here.

    root/
        |--after.txt
        |--after_.txt

    You can confirm path that under bar is added.

    Args:
        path (Path): Path you want to convert with avoiding existing path.

    Returns:
        Path: Path to avoid override of path.
    """
    while path.exists():
        path = path.with_stem(path.stem + "_")

    return path
