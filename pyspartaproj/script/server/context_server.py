#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from pathlib import Path
from typing import Dict

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import StrPair, Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.json.convert_from_json import (
    integer_pair_from_json, path_pair_from_json, string_pair_from_json)
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.modify.get_absolute import get_absolute


class ContextServer:
    def _get_table(self) -> StrPair:
        return {
            'timeout': 'integer',
            'port': 'integer',
            'host': 'string',
            'user_name': 'string',
            'private_key': 'path',
            'remote_root': 'path',
            'local_root': 'path'
        }

    def get_context_table(self, type: str) -> Strs:
        table: StrPair = self._get_table()
        return [key for key, value in table.items() if value == type]

    def _get_vscode_table(self) -> StrPair:
        return {
            'host': 'host',
            'username': 'user_name',
            'privateKeyPath': 'private_key',
            'remotePath': 'remote_root',
            'context': 'local_root',
            'connectTimeout': 'timeout',
            'port': 'port'
        }

    def _from_vscode(self, context: Json) -> Json:
        vscode_table: StrPair = self._get_vscode_table()

        if not isinstance(context, Dict):
            return {}

        return {
            vscode_table[key]: value
            for key, value in context.items()
            if key in vscode_table
        }

    def revert_default(self) -> None:
        self._current_context = deepcopy(self._default_context)

    def _load_default(self) -> None:
        self._default_context: Json = self._from_vscode(
            json_import(get_absolute(Path('.vscode', 'sftp.json')))
        )

        self.revert_default()

    def __init__(self) -> None:
        self._load_default()

    def get_integer(self, type: str) -> int:
        context: IntPair = integer_pair_from_json(self._current_context)
        return context[type]

    def get_string(self, type: str) -> str:
        context: StrPair = string_pair_from_json(self._current_context)
        return context[type]

    def get_path(self, type: str) -> Path:
        context: PathPair = path_pair_from_json(self._current_context)
        return context[type]

    def set_path(self, type: str, path: Path) -> bool:
        if type in self.get_context_table('path'):
            if isinstance(self._current_context, Dict):
                self._current_context[type] = path.as_posix()
                return True

        return False
