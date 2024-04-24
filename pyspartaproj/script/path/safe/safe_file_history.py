#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to record paths which is source and destination pair."""

from copy import deepcopy
from itertools import count
from pathlib import Path

from pyspartaproj.context.extension.path_context import PathPair2
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.directory.create_directory_temporary import WorkSpace
from pyspartaproj.script.directory.create_directory_working import (
    create_working_space,
)
from pyspartaproj.script.file.json.convert_to_json import multiple2_to_json
from pyspartaproj.script.file.json.export_json import json_export
from pyspartaproj.script.time.current_datetime import get_current_time


class FileHistory(WorkSpace):
    """Class to record paths which is source and destination pair.

    The module is used for e.g., custom copy or rename operation.
    """

    def _get_working_root(self, path: Path | None) -> Path:
        if path is None:
            path = self.get_root()

        return create_working_space(path, jst=True)

    def _initialize_paths(self, working_root: Path) -> None:
        self._working_root: Path = working_root
        self._history_root: Path = self.create_sub_directory("history")

    def _initialize_variables(self, history_path: Path | None) -> None:
        self._still_removed: bool = False
        self._history: PathPair2 = {}

        self._initialize_paths(self._get_working_root(history_path))

    def _export_history(self, history: Json) -> bool:
        export_path: Path = self.get_history_path()

        if export_path.parent.exists():
            json_export(export_path, history)
            return True

        return False

    def _get_key_time(self) -> str:
        time: str = get_current_time(jst=True).isoformat()

        for i in count():
            time_index: str = time + "_" + str(i).zfill(4)

            if time_index not in self._history:
                return time_index

        return ""

    def _clear_history(self) -> PathPair2 | None:
        if 0 == len(self._history):
            return None

        history: PathPair2 = deepcopy(self._history)
        self._history.clear()

        return history

    def _finalize_history(self) -> PathPair2 | None:
        history: PathPair2 | None = self.get_history()

        super().__del__()

        return history

    def create_sub_directory(self, group: str) -> Path:
        """Create sub directory in temporary working space.

        Args:
            group (str): Name of directory you want to create.

        Returns:
            Path: Path of created sub directory.
        """
        return create_directory(Path(self._working_root, group))

    def get_history(self) -> PathPair2 | None:
        """Get and initialize the history of file operation.

        Returns:
            PathPair2 | None: The history of file operation until current.
        """
        if history := self._clear_history():
            if self._export_history(multiple2_to_json(history)):
                return history

        return None

    def get_history_path(self) -> Path:
        """Get path of file which contain the history of file operation.

        Returns:
            Path: Path of file operation history.
        """
        return Path(self._history_root, "history.json")

    def add_history(self, source_path: Path, destination_path: Path) -> None:
        """Record paths which is source and destination pair.

        Args:
            source_path (Path): Path witch is about "source" of file operation.

            destination_path (Path):
                Path witch is about "destination" of file operation.
        """
        self._history[self._get_key_time()] = {
            "source.path": source_path,
            "destination.path": destination_path,
        }

    def close_history(self) -> PathPair2 | None:
        """Closing process is executed just once.

        Returns:
            Path | None: Path of file including history of file operation.
        """
        if self._still_removed:
            return None

        self._still_removed = True

        return self._finalize_history()

    def __del__(self) -> None:
        """Export paths to temporary working space, and cleanup it."""
        self.close_history()

    def __init__(self, history_path: Path | None = None) -> None:
        """Initialize variables about path you want to record.

        Args:
            history_path (Path | None, optional): Defaults to None.
                Export directory of Json file witch paths is recorded.
        """
        super().__init__()

        self._initialize_variables(history_path)
