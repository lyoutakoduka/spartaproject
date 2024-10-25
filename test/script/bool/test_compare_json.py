#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.file.json_context import Json, Singles
from pyspartaproj.script.bool.compare_json import is_same_json


def _compare_json(left: Json, right: Json) -> None:
    assert is_same_json(left, right)


def test_single() -> None:
    _compare_json({"A": True}, {"A": True})


def test_nest() -> None:
    _compare_json({"A": {"B": True}}, {"A": {"B": True}})


def test_multiple() -> None:
    _compare_json({"A": True, "B": False}, {"B": False, "A": True})


def test_array() -> None:
    _compare_json({"A": ["B", "C"]}, {"A": ["B", "C"]})


def test_type() -> None:
    sources: Singles = [None, True, 0, 0.1, "test"]

    for source in sources:
        _compare_json(source, source)
