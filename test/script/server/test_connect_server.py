#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.server.connect_server import ConnectServer


def test_connect() -> None:
    server: ConnectServer = ConnectServer()
    assert server.connect()


def main() -> bool:
    test_connect()
    return True
