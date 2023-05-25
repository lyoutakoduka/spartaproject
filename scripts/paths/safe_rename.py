#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move

from contexts.path_context import Path, PathPair2
from scripts.files.convert_to_json import multiple2_to_json
from scripts.files.export_json import json_export
from scripts.paths.avoid_duplication import get_avoid_path
from scripts.paths.working_space import current_working_space
from scripts.times.current_datetime import get_current_time


class SafeRename:
    def __init__(self, history_path: Path = Path()) -> None:
        self._history: PathPair2 = {}
        self._init_history_path(history_path)

    def _init_history_path(self, path: Path) -> None:
        if '.' == str(path):
            path = current_working_space(Path('.trash'), jst=True)
        self.history_path: Path = path

    def __del__(self) -> None:
        self.pop_history()

    def pop_history(self) -> Path:
        if 0 == len(self._history):
            return self.history_path

        rename_path: Path = json_export(
            Path(self.history_path, 'rename.json'),
            multiple2_to_json(self._history),
        )
        self._history.clear()
        return rename_path

    def _add_history(self, source_path: Path, destination_path: Path) -> None:
        self._history[get_current_time(jst=True).isoformat()] = {
            'source': source_path,
            'destination': destination_path,
        }

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

        self._add_history(source_path, destination_path)

        return destination_path
