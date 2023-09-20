#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import count

from spartaproject.context.extension.path_context import Path, PathPair2
from spartaproject.context.file.json_context import Json
from spartaproject.script.directory.create_directory_temporary import WorkSpace
from spartaproject.script.directory.create_directory_working import \
    create_working_space
from spartaproject.script.file.json.convert_to_json import multiple2_to_json
from spartaproject.script.file.json.export_json import json_export
from spartaproject.script.time.current_datetime import get_current_time


class FileHistory(WorkSpace):
    def __init__(self, history_path: Path = Path()) -> None:
        super().__init__()

        self._history: PathPair2 = {}
        self.history_path: Path = self._init_history_path(history_path)

    def __del__(self) -> None:
        self.pop_history()

        super().__del__()

    def _init_history_path(self, path: Path) -> Path:
        if '.' == str(path):
            path = Path(self.get_root(), 'trash')

        return create_working_space(path, jst=True)

    def _export_history(self, history: Json) -> Path:
        return json_export(Path(self.history_path, 'rename.json'), history)

    def pop_history(self) -> Path:
        if 0 == len(self._history):
            return self.history_path

        history: Json = multiple2_to_json(self._history)
        self._history.clear()
        return self._export_history(history)

    def _get_key_time(self) -> str:
        time: str = get_current_time(jst=True).isoformat()

        for i in count():
            time_index: str = '_'.join([time, str(i).zfill(4)])
            if time_index not in self._history:
                return time_index
        return ''

    def add_history(self, source_path: Path, destination_path: Path) -> None:
        self._history[self._get_key_time()] = {
            'source': source_path, 'destination': destination_path
        }
