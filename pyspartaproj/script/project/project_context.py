#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to import a context of whole project from outside Json."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import StrPair, Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.json.convert_from_json import (
    integer_pair2_from_json,
    path_pair2_from_json,
    path_pair_from_json,
    string_pair2_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.modify.get_resource import get_resource


class ProjectContext:
    """Class to import a context of whole project."""

    def _get_context_path(self, forward: Path | None) -> Path:
        if forward is None:
            return get_resource(Path("project_context.json"))

        return forward

    def _load_context(self, forward: Path) -> Json:
        return json_import(
            path_pair_from_json(json_import(forward))["forward.path"]
        )

    def _serialize_path(self, base_context: Json) -> None:
        self._integer_context = integer_pair2_from_json(base_context)
        self._string_context = string_pair2_from_json(base_context)
        self._path_context = path_pair2_from_json(base_context)

    def __init__(self, forward: Path | None = None) -> None:
        """Import a project context file.

        The path of the context file is defined at a path forwarding file.

        e.g. in the following cases
        The project context file named "config.json"
        The path forwarding file named "forward.json"

        ProjectContext module import "forward.json" first,
            then find a path of "config.json" in therefore,
            finally import it.

        Args:
            forward (Path | None, optional): Defaults to None.
                alternative path of the path forwarding file,
                and mainly used at test of this module.
        """
        self._serialize_path(
            self._load_context(self._get_context_path(forward))
        )

    def get_integer_context(self, group: str) -> IntPair:
        """Filter and get project context by integer type.

        Args:
            group (str): select group of project context

        Returns:
            IntPair: project context of integer type
        """
        return self._integer_context[group]

    def get_string_context(self, group: str) -> StrPair:
        """Filter and get project context by string type.

        Args:
            group (str): select group of project context

        Returns:
            StrPair: project context of string type
        """
        return self._string_context[group]

    def get_path_context(self, group: str) -> PathPair:
        """Filter and get project context by path type.

        Args:
            group (str): select group of project context

        Returns:
            PathPair: project context of path type
        """
        return self._path_context[group]

    def get_platform_key(self, keys: Strs) -> str:
        return "_".join(keys + [uname().system.lower()])

    def merge_platform_path(
        self, group: str, path_type: str, file_type: str
    ) -> Path:
        context_types: Strs = [
            self.get_platform_key([context_type])
            for context_type in [path_type, file_type]
        ]

        return Path(
            self.get_path_context(group)[context_types[0] + ".path"],
            self.get_string_context(group)[context_types[1]],
        )
