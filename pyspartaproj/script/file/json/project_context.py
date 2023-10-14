#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import StrPair
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.json.convert_from_json import (
    integer_pair2_from_json,
    path_pair_from_json,
    string_pair2_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import


class ProjectContext:
    def _get_context_path(self, forward: Path | None) -> Path:
        if forward is None:
            return Path("pyspartaproj", "resource", "project_context.json")

        return forward

    def _load_context(self, forward: Path) -> Json:
        return json_import(
            path_pair_from_json(json_import(forward))["forward.path"]
        )

    def _serialize_path(self, base_context: Json) -> None:
        self._integer_context = integer_pair2_from_json(base_context)
        self._string_context = string_pair2_from_json(base_context)

    def __init__(self, forward: Path | None = None) -> None:
        self._serialize_path(
            self._load_context(self._get_context_path(forward))
        )

    def get_integer_context(self, group: str) -> IntPair:
        return self._integer_context[group]

    def get_string_context(self, group: str) -> StrPair:
        return self._string_context[group]
