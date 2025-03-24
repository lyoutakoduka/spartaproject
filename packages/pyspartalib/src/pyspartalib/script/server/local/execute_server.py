#!/usr/bin/env python

"""Module to execute python code on server you can use ssh connection."""

from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.error.error_raise import (
    ErrorContain,
    ErrorFail,
    ErrorNone,
)
from pyspartalib.script.server.local.upload_server import UploadServer
from pyspartalib.script.server.script_version import get_version_name


class _ErrorIdentifier:
    def _get_filter_head(self) -> str:
        return "traceback".capitalize()

    def _error_strings(self) -> Strs:
        return ["most", "recent", "call", "last"]

    def _get_filter_inside(self) -> str:
        return " ".join(self._error_strings())

    def _get_filter_body(self) -> str:
        return "(" + self._get_filter_inside() + ")"

    def get_identifier(self) -> str:
        return self._get_filter_head() + " " + self._get_filter_body() + ":"


class _RuntimeLocal:
    def _set_version(self, version: str | None) -> str:
        if version is None:
            version = "3.11.5"

        return get_version_name(version)

    def _get_local(self) -> Path:
        return Path("bin", "python3")

    def get_path(self, version: str | None) -> Path:
        return Path(self._set_version(version), self._get_local())


class ExecuteServer(UploadServer, ErrorContain, ErrorNone, ErrorFail):
    """Class to execute python code on server."""

    def __initialize_super_class(
        self,
        local_root: Path | None,
        override: bool,
        jst: bool,
        forward: Path | None,
        platform: str | None,
    ) -> None:
        super().__init__(
            local_root=local_root,
            override=override,
            jst=jst,
            forward=forward,
            platform=platform,
        )

    def __initialize_variables(self, version: str | None) -> None:
        self._runtime_path: Path = self._get_runtime_path(version)
        self._error_identifier: str = self._get_error_identifier()

    def _initialize_path(self, source_root: Path) -> None:
        self._source_root = source_root

    def _get_runtime_path(self, version: str | None) -> Path:
        return Path(
            self.get_path("python_root"),
            _RuntimeLocal().get_path(version),
        )

    def _get_error_identifier(self) -> str:
        return _ErrorIdentifier().get_identifier()

    def _get_command(self) -> Strs:
        return [
            path.as_posix()
            for path in [
                self._runtime_path,
                self.to_relative_path(self._source_root),
            ]
        ]

    def _execute_command(self) -> Strs | None:
        return self.execute_ssh(self._get_command())

    def _confirm_upload(self) -> None:
        self.error_fail(self.upload(self._source_root), "server")

    def _confirm_execute(self) -> Strs:
        return self.error_none_walrus(self._execute_command(), "server")

    def execute(self, source_root: Path) -> Strs:
        """Execute Python code you selected.

        Args:
            source_root (Path):
                Local path of Python code you will upload and execute.

        Returns:
            Strs | None:
                Stdout of executed Python code when execution is successful.

        """
        self._initialize_path(source_root)

        self._confirm_upload()

        result: Strs = self._confirm_execute()

        self.error_contain(
            "\n".join(result),
            self._error_identifier,
            "server",
            invert=True,
        )

        return result

    def __init__(
        self,
        version: str | None = None,
        local_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
        forward: Path | None = None,
        platform: str | None = None,
    ) -> None:
        """Select version of Python, then ready using ssh and sftp connection.

        Args:
            version (str | None, optional): Defaults to None.
                Version information of Python you want to execute.

            local_root (Path | None, optional): Defaults to None.
                User defined path of local working space which is used.
                It's used for argument "local_root" of class "UploadServer".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of class "UploadServer".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of class "UploadServer".

            forward (Path | None, optional): Defaults to None.
                Path of setting file in order to place
                    project context file to any place.
                It's used for argument "forward" of class "UploadServer".

            platform (str | None, optional): Defaults to None.
                Platform information should be "linux" or "windows",
                    and it's used in the project context file like follow.
                It's used for argument "platform" of class "UploadServer".

        """
        self.__initialize_super_class(
            local_root,
            override,
            jst,
            forward,
            platform,
        )
        self.__initialize_variables(version)
