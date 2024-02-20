#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to take out directory from inside of archive as archive."""

from pathlib import Path

from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.file.archive.edit_zip import EditZip
from pyspartaproj.script.path.iterate_directory import walk_iterator


def _get_took_out(decompressed_root: Path) -> Paths:
    archive_paths: Paths = []

    for directory_root in walk_iterator(decompressed_root, file=False):
        if 0 < len(list(walk_iterator(directory_root, directory=False))):
            archive_paths = [directory_root]

    return archive_paths


def take_out_zip(archive_path: Path) -> Paths:
    """Take out directory from inside of archive as archive.

    Args:
        archive_path (Path): Path of archive you want to take out.

    Returns:
        Paths: List of directory path which is took out.
    """
    edit_zip = EditZip(archive_path)
    return _get_took_out(edit_zip.get_decompressed_root())
