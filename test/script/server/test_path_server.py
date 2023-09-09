#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Callable

from script.server.path_server import PathServer


def _common_test(function: Callable[[PathServer], None]) -> None:
    server: PathServer = PathServer()
    function(server)


def test_table() -> None:
    EXPECTED: int = 3

    def individual_test(server: PathServer) -> None:
        assert EXPECTED == len(
            [type for type in server.get_path_table()]
        )

    _common_test(individual_test)


def test_path() -> None:
    def individual_test(server: PathServer) -> None:
        for type in server.get_path_table():
            server.get_path(type)
            assert True

    _common_test(individual_test)


def test_path_string() -> None:
    def individual_test(server: PathServer) -> None:
        for type in server.get_context_table('path'):
            assert server.get_path(type) == Path(server.get_path_string(type))

    _common_test(individual_test)


def main() -> bool:
    test_table()
    test_path()
    test_path_string()
    return True
