#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Callable

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.script.server.local.context_server import ContextServer


def _common_test(function: Callable[[ContextServer], None]) -> None:
    server: ContextServer = ContextServer()
    function(server)


def test_key() -> None:
    EXPECTED: int = 7

    def individual_test(server: ContextServer) -> None:
        assert EXPECTED == sum(
            [
                len(function())
                for function in [
                    server.get_integer_table,
                    server.get_string_table,
                    server.get_path_table,
                ]
            ]
        )

    _common_test(individual_test)


def test_integer() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in server.get_integer_table():
            assert isinstance(server.get_integer(type), int)

    _common_test(individual_test)


def test_string() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in server.get_string_table():
            assert isinstance(server.get_string(type), str)

    _common_test(individual_test)


def test_path() -> None:
    def individual_test(server: ContextServer) -> None:
        for type in server.get_path_table():
            assert isinstance(server.get_path(type), Path)

    _common_test(individual_test)


def test_set_path() -> None:
    expected: Path = Path(__file__)

    def individual_test(server: ContextServer) -> None:
        for type in server.get_path_table():
            server.set_path(type, expected)
            assert expected == server.get_path(type)

    _common_test(individual_test)


def test_revert() -> None:
    input: Path = Path(__file__)

    def individual_test(server: ContextServer) -> None:
        for type in server.get_path_table():
            current: Path = server.get_path(type)
            server.set_path(type, input)
            server.revert_default()
            assert current == server.get_path(type)

    _common_test(individual_test)


def main() -> bool:
    test_key()
    test_integer()
    test_string()
    test_path()
    test_set_path()
    test_revert()
    return True
