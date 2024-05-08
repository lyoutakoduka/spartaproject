#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to use SSH and SFTP functionality."""

from pyspartaproj.interface.paramiko import Channel, SSHClient
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.server.local.connect_server import ConnectServer


def _is_connect() -> ConnectServer:
    server = ConnectServer()

    if server.connect():
        return server

    fail()


def test_connect() -> None:
    """Test to connect server by using SSH and SFTP functionality."""
    _is_connect()


def test_ssh() -> None:
    if server := _is_connect():
        assert isinstance(server.get_ssh(), SSHClient)


def test_channel() -> None:
    if server := _is_connect():
        assert isinstance(server.get_channel(), Channel)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_connect()
    test_ssh()
    test_channel()
    return True
