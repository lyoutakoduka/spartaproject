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
    def revert_default(self) -> None:
        self._current_context = deepcopy(self._default_context)

    def _load_default(self) -> None:
        context: Json = json_import(Path(Path.cwd(), "spartaproject.json"))
        if isinstance(context, Dict):
            self._default_context: Json = context["server"]

        self.revert_default()

    def __init__(self) -> None:
        self._load_default()

    def _filter_integer(self) -> IntPair:
        return integer_pair_from_json(self._current_context)

    def _filter_string(self) -> StrPair:
        return string_pair_from_json(self._current_context)

    def _filter_path(self) -> PathPair:
        return path_pair_from_json(self._current_context)

    def get_integer_context(self, type: str) -> int:
        context: IntPair = self._filter_integer()
        return context[type]

    def get_string_context(self, type: str) -> str:
        context: StrPair = self._filter_string()
        return context[type]

    def get_path_context(self, type: str) -> Path:
        context: PathPair = self._filter_path()
        return context[type]

    def get_integer_context_keys(self) -> Strs:
        context_integer: IntPair = self._filter_integer()
        return list(context_integer.keys())

    def get_string_context_keys(self) -> Strs:
        context_string: StrPair = self._filter_string()
        return list(context_string.keys())

    def get_path_context_keys(self) -> Strs:
        context_path: PathPair = self._filter_path()
        return list(context_path.keys())

    def set_path_context(self, type: str, path: Path) -> bool:
        if type in self.get_path_context_keys():
            if isinstance(self._current_context, Dict):
                self._current_context[type] = path.as_posix()
                return True

        return False
