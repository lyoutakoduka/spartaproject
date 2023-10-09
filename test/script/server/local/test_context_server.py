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
    expected: Ints = [2, 2, 3]

    def individual_test(server: ContextServer) -> None:
        assert expected == [
            len(function())
            for function in [
                server.get_integer_context_keys,
                server.get_string_context_keys,
                server.get_path_context_keys,
            ]
        ]

    _common_test(individual_test)


def test_integer() -> None:
    def individual_test(server: ContextServer) -> None:
        for context_key in server.get_integer_context_keys():
            assert isinstance(server.get_integer_context(context_key), int)

    _common_test(individual_test)


def test_string() -> None:
    def individual_test(server: ContextServer) -> None:
        for context_key in server.get_string_context_keys():
            assert isinstance(server.get_string_context(context_key), str)

    _common_test(individual_test)


def test_path() -> None:
    def individual_test(server: ContextServer) -> None:
        for context_key in server.get_path_context_keys():
            assert isinstance(server.get_path_context(context_key), Path)

    _common_test(individual_test)


def test_set_path() -> None:
    expected: Path = Path(__file__)

    def individual_test(server: ContextServer) -> None:
        for context_key in server.get_path_context_keys():
            server.set_path_context(context_key, expected)
            assert expected == server.get_path_context(context_key)

    _common_test(individual_test)


def test_revert() -> None:
    context_value: Path = Path(__file__)

    def individual_test(server: ContextServer) -> None:
        for context_key in server.get_path_context_keys():
            expected: Path = server.get_path_context(context_key)
            server.set_path_context(context_key, context_value)
            server.revert_default()
            assert expected == server.get_path_context(context_key)

    _common_test(individual_test)


def main() -> bool:
    test_key()
    test_integer()
    test_string()
    test_path()
    test_set_path()
    test_revert()
    return True
