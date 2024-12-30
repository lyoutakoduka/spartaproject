#!/usr/bin/env python

"""Module to upload file or directory by SFTP functionality."""

from os import stat_result
from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import Paths
from pyspartalib.interface.paramiko import SFTPAttributes
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartalib.script.server.local.connect_server import ConnectServer


class UploadServer(ConnectServer):
    """Class to upload file or directory by SFTP functionality."""

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

    def _get_remote_root(self) -> Path | None:
        if (sftp := self.get_sftp()) is None:
            return None

        if (root := sftp.getcwd()) is None:
            return None

        return Path(root)

    def _get_server_tree(self, path: Path, remote: Path) -> Paths:
        tree: Paths = []

        for parent in path.parents:
            if not is_relative(parent, root_path=remote):
                continue

            if str(get_relative(parent, root_path=remote)) != ".":
                tree += [parent]

        return tree

    def _get_upload_tree(self, path: Path) -> Paths | None:
        if remote := self._get_remote_root():
            return self._get_server_tree(path, remote)

        return None

    def _exists_directory(self, path: Path) -> bool:
        if (sftp := self.get_sftp()) is None:
            return False

        return path.name in sftp.listdir(path.parent.as_posix())

    def _create_directory(self, path: Path) -> None:
        if (sftp := self.get_sftp()) and (not self._exists_directory(path)):
            sftp.mkdir(path.as_posix())

    def _create_upload_tree(self, path: Path) -> None:
        if paths := self._get_upload_tree(path):
            for path_child in reversed(paths):
                self._create_directory(path_child)

    def _convert_remote_path(self, local: Path) -> Path | None:
        if remote_root := self._get_remote_root():
            return Path(remote_root, local)

        return None

    def _paths_to_strings(self, source: Path, destination: Path) -> Strs:
        return [path.as_posix() for path in [source, destination]]

    def _get_size_local(self, path: Path) -> int:
        return path.stat().st_size

    def _get_size_server(self, source: str, destination: str) -> int | None:
        if (sftp := self.get_sftp()) is None:
            return False

        return sftp.put(source, destination).st_size

    def _create_file(self, source: Path, destination: Path) -> bool:
        texts: Strs = self._paths_to_strings(source, destination)

        if (size_server := self._get_size_server(texts[0], texts[1])) is None:
            return False

        return self._get_size_local(source) == size_server

    def _path_with_tree(self, local: Path) -> Path | None:
        if path := self._convert_remote_path(local):
            self._create_upload_tree(path)
            return path

        return None

    def _upload_file(self, source: Path, destination_local: Path) -> bool:
        if destination := self._path_with_tree(destination_local):
            return self._create_file(source, destination)

        return False

    def _upload_directory(self, local: Path) -> None:
        if path := self._path_with_tree(local):
            self._create_directory(path)

    def _upload_tree(self, source: Path, destination_local: Path) -> bool:
        self._upload_directory(destination_local)

        for source_child in walk_iterator(source, depth=1):
            if not self._upload(
                source_child,
                Path(
                    destination_local,
                    get_relative(source_child, root_path=source),
                ),
            ):
                return False

        return True

    def _upload(self, source: Path, destination_local: Path) -> bool:
        if source.is_dir():
            return self._upload_tree(source, destination_local)

        return self._upload_file(source, destination_local)

    def upload(self, source: Path, destination: Path | None = None) -> bool:
        """Upload file or directory by SFTP functionality.

        Args:
            source (Path): Local path of file or directory you want to upload.

            destination (Path | None, optional): Defaults to None.
                Uploaded path of file or directory on server.

        Returns:
            bool: True if uploading succeed.

        """
        if destination is None:
            destination = self.to_relative_path(source)

        return self._upload(source, destination)

    def __init__(
        self,
        local_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
        forward: Path | None = None,
        platform: str | None = None,
    ) -> None:
        """Initialize super class.

        Args:
            local_root (Path | None, optional): Defaults to None.
                User defined path of local working space which is used.
                It's used for argument "local_root" of class "ConnectServer".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of class "ConnectServer".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of class "ConnectServer".

            forward (Path | None, optional): Defaults to None.
                Path of setting file in order to place
                    project context file to any place.
                It's used for argument "forward" of class "ConnectServer".

            platform (str | None, optional): Defaults to None.
                Platform information should be "linux" or "windows",
                    and it's used in the project context file like follow.
                It's used for argument "platform" of class "ConnectServer".

        """
        self.__initialize_super_class(
            local_root,
            override,
            jst,
            forward,
            platform,
        )
