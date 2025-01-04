#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to check that two Json objects are same."""

from pyspartalib.context.file.json_context import Json, Singles
from pyspartalib.script.bool.compare_json import is_same_json


def _compare_json(left: Json, right: Json) -> None:
    assert is_same_json(left, right)


def test_single() -> None:
    """Test to compare simple two Json objects."""
    _compare_json({"A": True}, {"A": True})


def test_nest() -> None:
    """Test to compare nested two Json objects."""
    _compare_json({"A": {"B": True}}, {"A": {"B": True}})


def test_multiple() -> None:
    """Test to compare two Json objects structured by multiple elements."""
    _compare_json({"A": True, "B": False}, {"B": False, "A": True})


def test_array() -> None:
    """Test to compare two Json objects including array value."""
    _compare_json({"A": ["B", "C"]}, {"A": ["B", "C"]})


def test_type() -> None:
    """Test to compare several types same value."""
    sources: Singles = [None, True, 0, 0.1, "test"]

    for source in sources:
        _compare_json(source, source)
