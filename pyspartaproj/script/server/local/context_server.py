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
    integer_pair_from_json,
    path_pair_from_json,
    string_pair_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import


class ContextServer:
    def _get_table(self) -> StrPair:
        return {
            "timeout": "integer",
            "port": "integer",
            "host": "string",
            "user_name": "string",
            "private_key": "path",
            "remote_root": "path",
            "local_root": "path",
        }

    def get_context_table(self, type: str) -> Strs:
        if "integer" == type:
            context_integer: IntPair = integer_pair_from_json(
                self._current_context
            )
            return list(context_integer.keys())

        elif "string" == type:
            context_string: StrPair = string_pair_from_json(
                self._current_context
            )
            return list(context_string.keys())

        elif "path" == type:
            context_path: PathPair = path_pair_from_json(self._current_context)
            return list(context_path.keys())

        return []

    def revert_default(self) -> None:
        self._current_context = deepcopy(self._default_context)

    def _load_default(self) -> None:
        context: Json = json_import(Path(Path.cwd(), "spartaproject.json"))
        if isinstance(context, Dict):
            self._default_context: Json = context["server"]

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
        if type in self.get_context_table("path"):
            if isinstance(self._current_context, Dict):
                self._current_context[type] = path.as_posix()
                return True

        return False
