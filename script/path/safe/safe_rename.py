#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move

from context.extension.path_context import Path
from script.path.modify.avoid_duplication import get_avoid_path
from script.path.safe.safe_file_history import FileHistory


class SafeRename(FileHistory):
    def rename(
        self, source_path: Path, destination_path: Path, override: bool = False
    ) -> Path:
        if override:
            destination_path = get_avoid_path(destination_path)

        move(source_path, destination_path)  # not use rename
        self.add_history(source_path, destination_path)

        return destination_path
