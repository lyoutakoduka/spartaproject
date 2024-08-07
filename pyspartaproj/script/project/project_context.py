#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to import a context of whole project from outside Json."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.bool_context import BoolPair, BoolPair2
from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.context.default.string_context import StrPair, StrPair2, Strs
from pyspartaproj.context.extension.path_context import PathPair, PathPair2
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.json.convert_from_json import (
    bool_pair2_from_json,
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
            return get_resource(
                local_path=Path("project_context", "forward.json")
            )

        return forward

    def _load_context(self, forward: Path) -> Json:
        return json_import(
            path_pair_from_json(json_import(forward))["forward.path"]
        )

    def _serialize_path(self, base_context: Json) -> None:
        self._bool_context: BoolPair2 = bool_pair2_from_json(base_context)
        self._integer_context: IntPair2 = integer_pair2_from_json(base_context)
        self._string_context: StrPair2 = string_pair2_from_json(base_context)
        self._path_context: PathPair2 = path_pair2_from_json(base_context)

    def _override_platform(self, platform: str | None) -> None:
        if platform is None:
            platform = uname().system.lower()

        self.platform = platform

    def _get_context_types(self, context_keys: Strs) -> StrPair:
        return {
            context_key: self.get_platform_key([context_key])
            for context_key in context_keys
        }

    def _merged_path_context(self, group: str, path_types: Strs) -> Path:
        context_types: StrPair = self._get_context_types(path_types)
        path_context: PathPair = self.get_path_context(group)

        return Path(
            *[
                path_context[context_types[path_type] + ".path"]
                for path_type in path_types
            ]
        )

    def _merged_string_context(
        self,
        group: str,
        file_type: str,
        platform_root: Path,
    ) -> Path:
        context_types: StrPair = self._get_context_types([file_type])

        return Path(
            platform_root,
            self.get_string_context(group)[context_types[file_type]],
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

    def merge_platform_path(
        self, group: str, path_types: Strs, file_type: str | None = None
    ) -> Path:
        """Get path merged with multiple directories and single file.

        The path is corresponding to platform,
            and created from project context file.

        e.g., the project context file for explaining is follow.

        {
            "group": {
                "file_linux": "file_B",
                "file_windows": "file_C",
                "group_linux.path": "root/group_B",
                "group_windows.path": "root/group_C",
                "directory_linux.path": "root/directory_B",
                "directory_windows.path": "root/directory_C"
            }
        }

        Args:
            group (str): Sub-group of the project context,
                select "group" if in the project context above.

            path_types (Strs):
                List of identifier of directory you want to merge,
                select ["group", "directory"] if in the project context above.

            file_type (str | None, optional): Defaults to None.
                Identifier of file you want to merge,
                select "file" if in the project context above.

        Returns:
            Path: Merged path corresponding to platform.

            If you select group is "group",
                path_types is ["group", "directory"],
                and file_type is "file" in Linux environment,
                "root/directory_B/file_B" is returned.
        """
        platform_root: Path = self._merged_path_context(group, path_types)

        if file_type is None:
            return platform_root

        return self._merged_string_context(group, file_type, platform_root)

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
        self._serialize_path(
            self._load_context(self._get_context_path(forward))
        )
        self._override_platform(platform)
