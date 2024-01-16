#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to rename file or directory and log history."""

from pathlib import Path
from shutil import move

from pyspartaproj.script.path.modify.avoid_duplication import get_avoid_path
from pyspartaproj.script.path.safe.safe_file_history import FileHistory


class SafeRename(FileHistory):
    """Class to rename file or directory and log history."""

    def rename(
        self, source_path: Path, destination_path: Path, override: bool = False
    ) -> Path:
        """Rename file or directory and log history.

        Args:
            source_path (Path): Path you want to rename.

            destination_path (Path): Path which is rename destination.

            override (bool, optional): Defaults to False.
                Add under bar to back of destination path
                if destination path is exists.

        Returns:
            Path: Final destination renamed path.
        """
        if override:
            destination_path = get_avoid_path(destination_path)

        move(source_path, destination_path)  # not use rename
        self.add_history(source_path, destination_path)

        return destination_path
