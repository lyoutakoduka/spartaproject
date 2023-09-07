#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Callable

from script.server.context_server import ContextServer


def _common_test(function: Callable[[ContextServer], None]) -> None:
    server: ContextServer = ContextServer()
    function(server)


def test_key() -> None:
    EXPECTED: int = 7

    def individual_test(server: ContextServer) -> None:
        assert EXPECTED == sum([
            len(server.get_table(type))
            for type in ['integer', 'string', 'path']
        ])

    _common_test(individual_test)


def test_integer() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in server.get_table('integer'):
            assert isinstance(server.get_integer(type), int)

    _common_test(individual_test)


def test_string() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in server.get_table('string'):
            assert isinstance(server.get_string(type), str)

    _common_test(individual_test)


def test_path() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in server.get_table('path'):
            assert isinstance(server.get_path(type), Path)

    _common_test(individual_test)


def main() -> bool:
    test_key()
    test_integer()
    test_string()
    test_path()
    return True
