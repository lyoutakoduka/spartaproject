#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to record paths which is source and destination pair."""

from copy import deepcopy
from itertools import count
from pathlib import Path

from pyspartalib.context.extension.path_context import PathPair2
from pyspartalib.script.directory.work_space import WorkSpace
from pyspartalib.script.file.json.convert_to_json import multiple2_to_json
from pyspartalib.script.file.json.export_json import json_export
from pyspartalib.script.time.stamp.current_datetime import get_current_time


class FileHistory(WorkSpace):
    """Class to record paths which is source and destination pair.

    The module is used for e.g., custom copy or rename operation.
    """

    def _initialize_variables_history(
        self, history_root: Path | None, override: bool, jst: bool
    ) -> None:
        self._still_removed: bool = False
        self._history: PathPair2 = {}
        self._history_path: Path | None = None
        self._history_root: Path = self.create_date_time_space(
            body_root=history_root, override=override, jst=jst
        )

    def _update_history_path(self) -> None:
        self._history_path = Path(
            self._history_root, self._get_key_time() + ".json"
        )

    def _export_history(self, history: PathPair2) -> None:
        if history_path := self.get_history_path():
            json_export(history_path, multiple2_to_json(history))

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

    def get_history_root(self) -> Path:
        """Get path of temporary working space including date time string.

        Returns:
            Path: Path of temporary working space.
        """
        return self._history_root

    def get_history_path(self) -> Path | None:
        """Get path of file which contain the history of file operation.

        Returns:
            Path: Path of file operation history.
        """
        return self._history_path

    def get_history(self) -> PathPair2 | None:
        """Get and initialize the history of file operation.

        Returns:
            PathPair2 | None: The history of file operation until current.
        """
        if history := self._clear_history():
            self._update_history_path()
            self._export_history(history)
            return history

        return None

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

    def __init__(
        self,
        working_root: Path | None = None,
        history_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
    ) -> None:
        """Initialize variables about path you want to record.

        Args:
            working_root (Path | None, optional): Defaults to None.
                User defined temporary working space.
                It's mainly used for test.
                It's used for argument "working_root" of class "WorkSpace".

            history_root (Path | None, optional): Defaults to None.
                User defined path of temporary working space
                    including date time string.
                It's used for argument "body_root" of
                    function "create_date_time_space".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of
                    function "create_date_time_space".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of
                    function "create_date_time_space".
        """
        super().__init__(working_root=working_root)

        self._initialize_variables_history(history_root, override, jst)
