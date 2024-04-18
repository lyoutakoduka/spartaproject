#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to record paths which is source and destination pair."""

from itertools import count
from pathlib import Path

from pyspartaproj.context.extension.path_context import PathPair2
from pyspartaproj.context.file.json_context import Json
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

    def _init_history_path(self, path: Path | None) -> Path:
        if path is None:
            path = Path(self.get_root(), "trash")

        return create_working_space(path, jst=True)

    def _initialize_variables(self, history_path: Path | None) -> None:
        self._still_removed: bool = False
        self._history: PathPair2 = {}
        self.history_path: Path = self._init_history_path(history_path)

    def _export_history(self, history: Json) -> Path:
        return json_export(
            Path(self.history_path, self.get_history_name()), history
        )

    def _get_key_time(self) -> str:
        time: str = get_current_time(jst=True).isoformat()

        for i in count():
            time_index: str = time + "_" + str(i).zfill(4)

            if time_index not in self._history:
                return time_index

        return ""

    def get_history_name(self) -> str:
        """Get name of file which contain the history of file operation.

        Returns:
            str: File name.
        """
        return "rename.json"

    def _pop_history(self) -> Path:
        """Export paths you record to temporary working space.

        Returns:
            Path: Path of exported Json file.
        """
        if 0 == len(self._history):
            return self.history_path

        history: Json = multiple2_to_json(self._history)
        self._history.clear()
        return self._export_history(history)

    def _finalize_history(self) -> Path | None:
        history_path: Path = self._pop_history()

        super().__del__()

        return history_path

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

    def __del__(self) -> None:
        """Export paths to temporary working space, and cleanup it."""
        self._finalize_history()

    def __init__(self, history_path: Path | None = None) -> None:
        """Initialize variables about path you want to record.

        Args:
            history_path (Path | None, optional): Defaults to None.
                Export directory of Json file witch paths is recorded.
        """
        super().__init__()

        self._initialize_variables(history_path)
