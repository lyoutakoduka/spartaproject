#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to take out directory from inside of archive as archive."""

from pathlib import Path

from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.file.archive.compress_zip import CompressZip
from pyspartaproj.script.file.archive.edit_zip import EditZip
from pyspartaproj.script.path.iterate_directory import walk_iterator


def _take_out_archive(
    took_out_root: Path, file_paths: Paths, archive_id: str
) -> Path:
    compress_zip = CompressZip(took_out_root, archive_id=archive_id)

    for file_path in file_paths:
        compress_zip.compress_archive(file_path)

    return compress_zip.close_archived()[0]


def _get_took_out(decompressed_root: Path) -> Paths:
    archive_paths: Paths = []

    for directory_root in walk_iterator(decompressed_root, file=False):
        file_paths: Paths = list(
            walk_iterator(directory_root, directory=False)
        )

        if 0 == len(file_paths):
            continue

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
