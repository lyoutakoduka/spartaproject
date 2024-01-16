#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to copy file or directory and log history."""

from pathlib import Path
from shutil import copy2, copytree

from pyspartaproj.script.path.modify.avoid_duplication import get_avoid_path
from pyspartaproj.script.path.safe.safe_file_history import FileHistory


class SafeCopy(FileHistory):
    """Class to copy file or directory and log history."""

    def copy(
        self, source_path: Path, destination_path: Path, override: bool = False
    ) -> Path:
        """Copy file or directory and log history.

        Args:
            source_path (Path): Path you want to copy.

            destination_path (Path): Path which is copy destination.

            override (bool, optional): Defaults to False.
                Add under bar to back of destination path
                if destination path is exists.

        Returns:
            Path: Final destination copied path.
        """
        if override:
            destination_path = get_avoid_path(destination_path)

        if source_path.is_dir():
            copytree(source_path, destination_path)
        else:
            copy2(source_path, destination_path)

        self.add_history(source_path, destination_path)

        return destination_path
