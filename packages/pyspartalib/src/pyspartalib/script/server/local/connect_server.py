#!/usr/bin/env python

"""Module to use SSH and SFTP functionality."""

from decimal import Decimal
from pathlib import Path
from time import sleep

from pyspartalib.context.default.string_context import StrPair, Strs
from pyspartalib.interface.paramiko import (
    AutoAddPolicy,
    Channel,
    SFTPClient,
    SSHClient,
)
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.project.project_context import ProjectContext
from pyspartalib.script.server.local.path_server import PathServer
from pyspartalib.script.string.encoding.set_decoding import set_decoding
from pyspartalib.script.string.encoding.set_encoding import set_encoding

initialize_decimal()


class ConnectServer(PathServer, ProjectContext):
    """Class to use SSH and SFTP functionality."""

    def __initialize_variables(self) -> None:
        self._split_identifier: str = "\x1b[?2004"
        self._ssh: SSHClient | None = None
        self._channel: Channel | None = None
        self._sftp: SFTPClient | None = None

    def __initialize_super_class(
        self,
        local_root: Path | None,
        override: bool,
        jst: bool,
        forward: Path | None,
        platform: str | None,
    ) -> None:
        PathServer.__init__(
            self,
            local_root=local_root,
            override=override,
            jst=jst,
        )
        ProjectContext.__init__(self, forward=forward, platform=platform)

    def _finalize_network_objects(self) -> None:
        if ssh := self.get_ssh():
            ssh.close()

        if sftp := self.get_sftp():
            sftp.close()

    def _get_passphrase(self) -> str:
        return self.get_string_context("server")[
            self.get_platform_key(["passphrase"])
        ]

    def _get_private_key(self) -> str:
        return self.get_path_context("server")[
            self.get_platform_key(["private", "key"]) + ".path"
        ].as_posix()

    def _get_timeout(self) -> float:
        milliseconds: int = self.get_integer_context("server")["timeout"]
        return float(Decimal(str(milliseconds)) / Decimal("1000.0"))

    def _connect_detail(self) -> None:
        string_context: StrPair = self.get_string_context("server")

        if ssh := self.get_ssh():
            ssh.connect(
                hostname=string_context["host"],
                username=string_context["user_name"],
                key_filename=self._get_private_key(),
                passphrase=self._get_passphrase(),
                port=self.get_integer_context("server")["port"],
                timeout=self._get_timeout(),
            )

    def _ssh_setting(self) -> None:
        if ssh := self.get_ssh():
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(AutoAddPolicy())

    def _create_ssh(self) -> None:
        self._ssh = SSHClient()

        self._ssh_setting()
        self._connect_detail()

    def _sleep(self) -> None:
        sleep(0.05)

    def _receive_byte(self) -> str | None:
        buffer: int = 9999

        if channel := self.get_channel():
            text_byte: bytes = b""

            for _ in range(2):
                if channel.recv_ready():
                    byte: bytes = channel.recv(buffer)
                    text_byte += byte
                    break

                self._sleep()

            return set_decoding(text_byte)

        return None

    def _extract_result(
        self,
        text: str,
        index: int,
        escape: str,
    ) -> str | None:
        lines: Strs = text.split(escape)
        correct_result: int = 2

        if len(lines) == correct_result:
            return lines[index]

        return None

    def _split_result(self, text: str) -> Strs:
        lines: Strs = text.split("\r\n")

        return [lines[0][1:]] + lines[1:-1]

    def _left_removed(self, text: str) -> str | None:
        return self._extract_result(text, -1, self._split_identifier + "l")

    def _right_removed(self, text: str) -> str | None:
        return self._extract_result(text, 0, self._split_identifier + "h")

    def _receive_ssh(self) -> Strs | None:
        if (
            (text := self._receive_byte())
            and (text := self._left_removed(text))
            and (text := self._right_removed(text))
        ):
            return self._split_result(text)

        return None

    def _execute_ssh(self, commands: Strs) -> None:
        command: str = " ".join(commands) + "\n"

        if channel := self.get_channel():
            channel.send(set_encoding(command))
            self._sleep()

    def _correct_path(self, result: Strs) -> bool:
        expected: Strs = [
            str(self.get_path(root))
            for root in ["private_root", "public_root"]
        ]

        return len({str(sorted(name)) for name in [expected, result]}) == 1

    def _ssh_correct_path(self) -> bool:
        return self._correct_path(
            [name[:-1] for name in self.execute_ssh(["ls", "-1", "-p"])],
        )

    def _get_remote_path(self) -> str:
        return self.get_path_context("server")["remote_root.path"].as_posix()

    def _create_channel_object(self) -> None:
        size: int = 1000

        if ssh := self.get_ssh():
            self._channel = ssh.invoke_shell(width=size, height=size)

    def _connect_ssh(self) -> bool:
        self._create_ssh()
        self._create_channel_object()
        self._receive_ssh()

        self.execute_ssh(["cd", self._get_remote_path()])
        return self._ssh_correct_path()

    def _receive_sftp(self) -> Strs:
        if sftp := self.get_sftp():
            return sftp.listdir()

        return []

    def _sftp_correct_path(self) -> bool:
        return self._correct_path(self._receive_sftp())

    def _sftp_remote_path(self) -> None:
        if sftp := self.get_sftp():
            sftp.chdir(self._get_remote_path())

    def _create_sftp(self) -> None:
        if ssh := self.get_ssh():
            self._sftp = ssh.open_sftp()

    def _connect_sftp(self) -> bool:
        self._create_sftp()

        self._sftp_remote_path()
        return self._sftp_correct_path()

    def get_ssh(self) -> SSHClient | None:
        """Get network object about SSH.

        Returns:
            SSHClient | None: Network object if exists.

        """
        return self._ssh

    def get_channel(self) -> Channel | None:
        """Get network object about shell of SSH.

        Returns:
            Channel | None: Network object if exists.

        """
        return self._channel

    def get_sftp(self) -> SFTPClient | None:
        """Get network object about SFTP.

        Returns:
            SFTPClient | None: Network object if exists.

        """
        return self._sftp

    def execute_ssh(self, commands: Strs) -> Strs | None:
        """Execute command by using SSH functionality.

        Args:
            commands (Strs): Elements of command which will merged by space.
                e.g., if command is "ls -la",
                you can input ["ls", "-la"] or ["ls -la"].

        Returns:
            Strs: Execution result of command.

        """
        self._execute_ssh(commands)
        return self._receive_ssh()

    def connect(self) -> bool:
        """Connect to server by using SSH and SFTP.

        Returns:
            bool: True if connecting process to server is success.

        """
        return self._connect_ssh() and self._connect_sftp()

    def __del__(self) -> None:
        """Close network objects."""
        self._finalize_network_objects()
        self.__initialize_variables()

    def __init__(
        self,
        local_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
        forward: Path | None = None,
        platform: str | None = None,
    ) -> None:
        """Initialize super class and network objects.

        Args:
            local_root (Path | None, optional): Defaults to None.
                User defined path of local working space which is used.
                It's used for argument "local_root" of class "PathServer".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of class "PathServer".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of class "PathServer".

            forward (Path | None, optional): Defaults to None.
                Path of setting file in order to place
                    project context file to any place.
                It's used for argument "forward" of class "ProjectContext".

            platform (str | None, optional): Defaults to None.
                Platform information should be "linux" or "windows",
                    and it's used in the project context file like follow.
                It's used for argument "platform" of class "ProjectContext".

        """
        self.__initialize_super_class(
            local_root,
            override,
            jst,
            forward,
            platform,
        )
        self.__initialize_variables()
