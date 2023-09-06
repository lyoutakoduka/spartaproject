#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Callable

from script.server.context_server import ContextServer


def _common_test(function: Callable[[ContextServer], None]) -> None:
    server: ContextServer = ContextServer()
    function(server)


def test_integer() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in ['timeout', 'port']:
            assert isinstance(server.get_integer(type), int)

    _common_test(individual_test)


def test_string() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in ['host', 'user_name']:
            assert isinstance(server.get_string(type), str)

    _common_test(individual_test)


def test_path() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in ['private_key', 'remote_root', 'local_root']:
            assert isinstance(server.get_path(type), Path)

    _common_test(individual_test)


def test_path_string() -> None:
    def individual_test(server: ContextServer) -> None:
        type: str = 'private_key'
        assert server.get_path(type) == Path(server.get_path_string(type))

    _common_test(individual_test)


def main() -> bool:
    test_integer()
    test_string()
    test_path()
    test_path_string()
    return True
