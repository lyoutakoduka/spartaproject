#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import SSHClient, SFTPClient, AutoAddPolicy, Channel
from pathlib import Path
from time import sleep
from typing import Dict

from context.default.integer_context import IntPair
from context.default.string_context import Strs, Strs2, StrPair
from context.extension.decimal_context import Decimal, set_decimal_context
from context.file.json_context import Json
from script.file.json.import_json import json_import
from script.path.modify.get_absolute import get_absolute

set_decimal_context()


class ConnectServer:
    def _filter_condition(self, key: str, ftp_context: Json) -> Json | None:
        if not isinstance(ftp_context, Dict):
            return None

        if key not in ftp_context:
            return None

        return ftp_context[key]

    def _get_type_text(self, ftp_context: Json) -> StrPair:
        context_texts: StrPair = {}

        for key in [
            'host', 'username', 'privateKeyPath', 'remotePath', 'context'
        ]:
            if value := self._filter_condition(key, ftp_context):
                if isinstance(value, str):
                    context_texts[key] = value

        return context_texts

    def _get_type_number(self, ftp_context: Json) -> IntPair:
        context_numbers: IntPair = {}

        for key in ['connectTimeout', 'port']:
            if value := self._filter_condition(key, ftp_context):
                if isinstance(value, int):
                    context_numbers[key] = value

        return context_numbers

    def _get_ftp_context(self) -> Json:
        ftp_context: Json = json_import(
            get_absolute(Path('.vscode', 'sftp.json'))
        )

        self._texts: StrPair = self._get_type_text(ftp_context)
        self._numbers: IntPair = self._get_type_number(ftp_context)

    def _initialize_connect(self) -> None:
        self._ssh: SSHClient | None = None
        self._shell: Channel | None = None
        self._sftp: SFTPClient | None = None

    def __init__(self) -> None:
        self._initialize_connect()
        self._get_ftp_context()

        self._EXPECTED: Strs = ['private', 'public']

    def get_ssh(self) -> SSHClient | None:
        return self._ssh

    def get_shell(self) -> Channel | None:
        return self._shell

    def get_sftp(self) -> SFTPClient | None:
        return self._sftp

    def get_type_text(self, type: str) -> str:
        return self._texts[type]

    def get_type_number(self, type: str) -> int:
        return self._numbers[type]

    def __del__(self) -> None:
        if ssh := self.get_ssh():
            ssh.close()

        if sftp := self.get_sftp():
            sftp.close()

        self._initialize_connect()

    def _connect_detail(self) -> None:
        milliseconds: int = self.get_type_number('connectTimeout')
        seconds: Decimal = Decimal(str(milliseconds)) / Decimal('1000.0')

        if ssh := self.get_ssh():
            ssh.connect(
                hostname=self.get_type_text('host'),
                port=self.get_type_number('port'),
                username=self.get_type_text('username'),
                key_filename=self.get_type_text('privateKeyPath'),
                timeout=float(seconds)
            )

    def _create_ssh(self) -> None:
        self._ssh = SSHClient()

        self._ssh.load_system_host_keys()
        self._ssh.set_missing_host_key_policy(AutoAddPolicy())

        self._connect_detail()

    def _sleep(self) -> None:
        sleep(0.01)

    def _receive_ssh(self) -> Strs:
        if shell := self.get_shell():
            self._sleep()

            while not shell.recv_ready():
                self._sleep()

            byte: bytes = shell.recv(9999)
            text: str = byte.decode('utf-8')

            lines: Strs = text.splitlines()
            return lines[2:-1]

        return []


    def _execute_ssh(self, commands: Strs) -> None:
        command: str = ' '.join(commands) + '\n'

        if shell := self.get_shell():
            shell.send(command.encode('utf-8'))

    def execute_ssh(self, commands: Strs) -> Strs:
        self._execute_ssh(commands)
        return self._receive_ssh()

    def _correct_path(self, expected: Strs, result: Strs) -> bool:
        name_sorted: Strs2 = [sorted(name) for name in [expected, result]]

        return name_sorted[0] == name_sorted[1]

    def _ssh_correct_path(self) -> bool:
        self._execute_ssh(['ls', '-1', '-p'])

        return self._correct_path(
            [name + '/' for name in self._EXPECTED], self._receive_ssh()
        )

    def _connect_ssh(self) -> bool:
        self._create_ssh()

        if ssh := self.get_ssh():
            self._shell = ssh.invoke_shell()

        self._receive_ssh()

        self.execute_ssh(['cd', self.get_type_text('remotePath')])
        return self._ssh_correct_path()

    def _receive_sftp(self) -> Strs:
        if sftp := self.get_sftp():
            return sftp.listdir()

        return []

    def _sftp_correct_path(self) -> bool:
        return self._correct_path(self._EXPECTED, self._receive_sftp())

    def _sftp_remote_path(self) -> None:
        if sftp := self.get_sftp():
            sftp.chdir(self.get_type_text('remotePath'))

    def _create_sftp(self) -> None:
        if ssh := self.get_ssh():
            self._sftp = ssh.open_sftp()

    def _connect_sftp(self) -> bool:
        self._create_sftp()

        self._sftp_remote_path()
        return self._sftp_correct_path()

    def connect(self) -> bool:
        if self._connect_ssh():
            if self._connect_sftp():
                return True

        return False
