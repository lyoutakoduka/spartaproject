#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert path to avoid existing path."""

from pathlib import Path


def get_avoid_path(path: Path) -> Path:
    """Function to convert path to avoid existing path.

    Args:
        path (Path): Path you want to convert with avoiding existing path.

    Returns:
        Path: Path to avoid existing path
    """
    while path.exists():
        path = path.with_stem(path.stem + "_")

    return path
