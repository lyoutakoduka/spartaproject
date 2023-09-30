#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable

from pyspartaproj.context.extension.path_context import Path
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.server.local.path_server import PathServer


def _common_test(function: Callable[[PathServer], None]) -> None:
    server: PathServer = PathServer()
    function(server)


def test_table() -> None:
    EXPECTED: int = 6

    def individual_test(server: PathServer) -> None:
        assert EXPECTED == len([type for type in server.get_path_table()])

    _common_test(individual_test)


def test_path() -> None:
    def individual_test(server: PathServer) -> None:
        for type in server.get_path_table():
            server.get_path(type)
            assert True

    _common_test(individual_test)


def test_to_remote() -> None:
    EXPECTED: Path = Path("temp")

    def individual_test(server: PathServer) -> None:
        assert EXPECTED == server.to_remote_path(
            Path(server.get_root(), EXPECTED)
        )

    _common_test(individual_test)


def test_to_local() -> None:
    EXPECTED: Path = Path("temp")

    def individual_test(server: PathServer) -> None:
        assert EXPECTED == server.to_remote_path(
            server.to_local_path(EXPECTED)
        )

    _common_test(individual_test)


def test_working() -> None:
    expected: Path = Path(
        "private", "work", "2023", "04", "01", "00", "00", "00", "000000"
    )

    def individual_test(server: PathServer) -> None:
        temporary_path: Path = server.get_working_space(override=True)

        assert temporary_path.exists()
        assert expected == get_relative(
            temporary_path, root_path=server.get_root()
        )

    _common_test(individual_test)


def main() -> bool:
    test_table()
    test_path()
    test_to_remote()
    test_to_local()
    test_working()
    return True
