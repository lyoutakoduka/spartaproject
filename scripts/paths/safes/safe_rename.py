#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move

from contexts.path_context import Path
from scripts.paths.avoid_duplication import get_avoid_path
from scripts.paths.safes.safe_file_history import FileHistory


class SafeRename(FileHistory):
    def rename(
        self, source_path: Path,
        destination_path: Path,
        override: bool = False,
    ) -> Path:
        if override:
            destination_path = get_avoid_path(destination_path)

        if source_path.drive == destination_path.drive:
            source_path.rename(destination_path)
        else:
            move(source_path, destination_path)  # to move other drive

        self.add_history(source_path, destination_path)

        return destination_path
