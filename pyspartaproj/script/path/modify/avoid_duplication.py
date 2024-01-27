#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert path which is avoiding existing path."""

from pathlib import Path


def get_avoid_path(path: Path) -> Path:
    """Function to convert path which is avoiding existing path.

    Args:
        path (Path): Path you want to convert with avoiding existing path.

    Returns:
        Path: Path which is avoiding existing path.
    """
    while path.exists():
        path = path.with_name(path.name + "_")

    return path
