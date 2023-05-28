#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import count

from contexts.json_context import Json
from contexts.path_context import Path, PathPair2
from scripts.files.jsons.convert_to_json import multiple2_to_json
from scripts.files.jsons.export_json import json_export
from scripts.paths.working_space import current_working_space
from scripts.times.current_datetime import get_current_time


class FileHistory:
    def __init__(self, history_path: Path = Path()) -> None:
        self._history: PathPair2 = {}
        self.history_path: Path = self._init_history_path(history_path)

    def __del__(self) -> None:
        self.pop_history()

    def _init_history_path(self, path: Path) -> Path:
        if '.' != str(path):
            return path
        return current_working_space(Path('.trash'), jst=True)

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
            'source': source_path,
            'destination': destination_path,
        }
