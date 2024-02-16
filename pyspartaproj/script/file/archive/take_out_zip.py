#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.file.archive.edit_zip import EditZip
from pyspartaproj.script.path.iterate_directory import walk_iterator


def _get_took_out(decompressed_root: Path) -> Paths:
    took_out: Paths = []

    for path in walk_iterator(decompressed_root, file=False):
        took_out = [path]

    return took_out


def take_out_zip(archive_path: Path) -> Paths:
    return _get_took_out(EditZip(archive_path).get_decompressed_root())
