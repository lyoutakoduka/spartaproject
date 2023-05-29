#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import copy2

from context.path_context import Path
from script.paths.avoid_duplication import get_avoid_path
from script.paths.safe.safe_file_history import FileHistory


class SafeCopy(FileHistory):
    def copy(
        self, source_path: Path,
        destination_path: Path,
        override: bool = False,
    ) -> Path:
        if override:
            destination_path = get_avoid_path(destination_path)

        copy2(source_path, destination_path)
        self.add_history(source_path, destination_path)

        return destination_path
