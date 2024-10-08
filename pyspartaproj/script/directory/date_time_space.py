#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create temporary working space including date time string."""

from pathlib import Path

from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.time.path.get_current_path import get_working_space


def create_working_space(
    root: Path, override: bool = False, jst: bool = False
) -> Path:
    """Create temporary working space that path include date time string.

    Args:
        root (Path): Directory path which temporary working space is created.

        override (bool, optional): Defaults to False.
            Override initial time count to "2023/4/1:12:00:00-00 (AM)".
            It's used for argument "override" of function "get_working_space".

        jst (bool, optional): Defaults to False.
            If True, you can get datetime object as JST time zone.
            It's used for argument "jst" of function "get_working_space".

    Returns:
        Path: End of directory path of created temporary working space.
    """
    return create_directory(
        Path(root, get_working_space(override=override, jst=jst))
    )
