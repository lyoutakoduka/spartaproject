#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

from context.default.integer_context import IntPair
from context.default.string_context import StrPair
from context.extension.path_context import Path, PathPair
from context.file.json_context import Json
from script.file.json.convert_from_json import (
    integer_pair_from_json,
    string_pair_from_json,
    path_pair_from_json
)
from script.file.json.import_json import json_import
from script.path.modify.get_absolute import get_absolute


class ContextServer:
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

    def _load_default(self) -> None:
        self._default_context: Json = self._from_vscode(
            json_import(get_absolute(Path('.vscode', 'sftp.json')))
        )

        self._current_context = self._default_context

    def __init__(self) -> None:
        self._load_default()

    def get_integer(self, type: str) -> int | None:
        context: IntPair = integer_pair_from_json(self._current_context)
        return context[type]

    def get_string(self, type: str) -> str | None:
        context: StrPair = string_pair_from_json(self._current_context)
        return context[type]

    def get_path(self, type: str) -> Path | None:
        context: PathPair = path_pair_from_json(self._current_context)
        return context[type]
