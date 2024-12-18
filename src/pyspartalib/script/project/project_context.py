#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to import a context of whole project from outside Json."""

from pathlib import Path

from pyspartalib.context.default.bool_context import BoolPair, BoolPair2
from pyspartalib.context.default.integer_context import IntPair, IntPair2
from pyspartalib.context.default.string_context import StrPair, StrPair2, Strs
from pyspartalib.context.extension.path_context import (
    PathPair,
    PathPair2,
    Paths,
)
from pyspartalib.context.file.json_context import Json
from pyspartalib.script.file.json.convert_from_json import (
    bool_pair2_from_json,
    integer_pair2_from_json,
    path_pair2_from_json,
    path_pair_from_json,
    string_pair2_from_json,
)
from pyspartalib.script.file.json.import_json import json_import
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.platform.platform_status import get_platform


class ProjectContext:
    """Class to import a context of whole project."""

    def _load_path_directly(self) -> Path:
        return get_resource(local_path=Path("project_context", "default.json"))

    def _get_forward_path(self, forward: Path) -> Path:
        return path_pair_from_json(json_import(forward))["forward.path"]

    def _get_context_path(self, forward: Path | None) -> Path:
        if forward is None:
            return self._load_path_directly()

        return self._get_forward_path(forward)

    def _serialize_path(self, base_context: Json) -> None:
        self._bool_context: BoolPair2 = bool_pair2_from_json(base_context)
        self._integer_context: IntPair2 = integer_pair2_from_json(base_context)
        self._string_context: StrPair2 = string_pair2_from_json(base_context)
        self._path_context: PathPair2 = path_pair2_from_json(base_context)

    def _override_platform(self, platform: str | None) -> None:
        if platform is None:
            platform = get_platform()

        self.platform: str = platform

    def _get_context_types(self, context_keys: Strs) -> StrPair:
        return {
            context_key: self.get_platform_key([context_key])
            for context_key in context_keys
        }

    def _get_path_elements(
        self, context_types: StrPair, path_context: PathPair, path_types: Strs
    ) -> Paths:
        return [
            path_context[context_types[path_type] + ".path"]
            for path_type in path_types
        ]

    def _merged_path_context(self, group: str, path_types: Strs) -> Path:
        return Path(
            *self._get_path_elements(
                self._get_context_types(path_types),
                self.get_path_context(group),
                path_types,
            )
        )

    def get_bool_context(self, group: str) -> BoolPair:
        """Filter and get project context by boolean type.

        Args:
            group (str): Select group of project context.

        Returns:
            BoolPair: Project context of boolean type.
        """
        return self._bool_context[group]

    def get_integer_context(self, group: str) -> IntPair:
        """Filter and get project context by integer type.

        Args:
            group (str): Select group of project context.

        Returns:
            IntPair: Project context of integer type.
        """
        return self._integer_context[group]

    def get_string_context(self, group: str) -> StrPair:
        """Filter and get project context by string type.

        Args:
            group (str): Select group of project context.

        Returns:
            StrPair: Project context of string type.
        """
        return self._string_context[group]

    def get_path_context(self, group: str) -> PathPair:
        """Filter and get project context by path type.

        Args:
            group (str): Select group of project context.

        Returns:
            PathPair: Project context of path type.
        """
        return self._path_context[group]

    def get_platform_key(self, keys: Strs) -> str:
        """Get key of project context corresponding to platform.

        Args:
            keys (Strs): Elements of key represented by string list.

            e.g., if you want to get key like "something_key_linux" in Linux,
                argument (keys) must ["something", "key"].

        Returns:
            str: The key corresponding to platform.
        """
        return "_".join(keys + [self.platform])

    def merge_platform_path(self, group: str, path_types: Strs) -> Path:
        """Get path merged with multiple path values.

        The path is corresponding to platform,
            and created from project context file.

        e.g., the project context file for explaining is follow.

        {
            "group": {
                "file_linux.path": "group/file_A",
                "file_windows.path": "group/file_B",
                "directory_linux.path": "root/directory_A",
                "directory_windows.path": "root/directory_B"
            }
        }

        Args:
            group (str): Sub-group of the project context,
                select "group" if in the project context above.

            path_types (Strs):
                List of identifier of directory you want to merge,
                select ["directory", "file"] if in the project context above.

        Returns:
            Path: Merged path corresponding to platform.

            If execution environment is Linux
                and you select group is "group"
                and path_types is ["directory", "file"].

            Path "root/directory_A/group/file_A" is returned.
        """
        return self._merged_path_context(group, path_types)

    def __init__(
        self, platform: str | None = None, forward: Path | None = None
    ) -> None:
        """Import a project context file.

        The path of the context file is defined at a path forwarding file.

        e.g., in the following cases.

        The project context file named "config.json"
        The path forwarding file named "forward.json"

        ProjectContext module import "forward.json" first,
            then find a path of "config.json" in therefore,
            finally import it.

        Default platform is automatically selected from current environment.

        Args:
            platform (str | None, optional): Defaults to None.
                Platform information should be "linux" or "windows",
                    and it's used in the project context file like follow.

                e.g., path type "key_linux.path", string type "key_windows".

            forward (Path | None, optional): Defaults to None.
                Path of setting file in order to place
                    project context file to any place.
        """
        self._serialize_path(json_import(self._get_context_path(forward)))
        self._override_platform(platform)
