#!/usr/bin/env python

"""Test module to use SSH and SFTP functionality."""

from pathlib import Path

from pyspartalib.interface.paramiko import Channel, SFTPClient, SSHClient
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.server.local.connect_server import ConnectServer


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_config_file() -> Path:
    return get_resource(local_path=Path("forward.json"))


def _is_connect() -> ConnectServer:
    server = ConnectServer(forward=_get_config_file())

    _fail_error(server.connect())

    return server


def test_connect() -> None:
    """Test to connect server by using SSH and SFTP functionality."""
    _is_connect()


def test_ssh() -> None:
    """Test to get network object about SSH."""
    if server := _is_connect():
        _fail_error(isinstance(server.get_ssh(), SSHClient))


def test_channel() -> None:
    """Test to get network object about shell of SSH."""
    if server := _is_connect():
        _fail_error(isinstance(server.get_channel(), Channel))


def test_ftp() -> None:
    """Test to get network object about SFTP."""
    if server := _is_connect():
        _fail_error(isinstance(server.get_sftp(), SFTPClient))
