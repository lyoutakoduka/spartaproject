#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test Module to get characters constructed by multiple or single byte."""

from pyspartalib.context.default.string_context import Strs, Strs2
from pyspartalib.context.typed.user_context import CharacterTable
from pyspartalib.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


def _compare_count(expected: int, table: Strs) -> None:
    assert expected == len(table)


def _compare_counts(tables: Strs2) -> None:
    for count, table in zip([26, 26, 10, 47], tables):
        _compare_count(count, table)


def _compare_both_ends(both_ends: Strs, table: Strs) -> None:
    assert both_ends == [table[-i] for i in range(2)]


def _compare_filtered(expected: Strs2, tables: Strs2) -> None:
    for both_ends, table in zip(expected, tables):
        _compare_both_ends(both_ends, table)


def _compare_size(result: CharacterTable) -> None:
    assert 4 == len(result)


def _get_tables(table: CharacterTable) -> Strs2:
    return [table["upper"], table["lower"], table["number"], table["other"]]


def _compare_table(expected: Strs2, result: CharacterTable) -> None:
    _compare_size(result)

    tables: Strs2 = _get_tables(result)

    _compare_counts(tables)
    _compare_filtered(expected, tables)


def _compare_merged(table: CharacterTable, merged: Strs2) -> None:
    assert _get_tables(table) == merged


def test_single() -> None:
    """Test to get characters constructed by single byte."""
    _compare_table(
        [["A", "Z"], ["a", "z"], ["0", "9"], [" ", "~"]],
        GroupedCharacters().get_table(),
    )


def test_multiple() -> None:
    """Test to get characters constructed by multiple byte."""
    _compare_table(
        [
            ["\uff21", "\uff3a"],
            ["\uff41", "\uff5a"],
            ["\uff10", "\uff19"],
            ["\u3000", "\uff5e"],
        ],
        GroupedCharacters(multiple=True).get_table(),
    )


def test_merge() -> None:
    """Test to compare merged character tables and originals."""
    grouped_characters = GroupedCharacters()

    _compare_merged(
        grouped_characters.get_table(), grouped_characters.get_merged_tables()
    )


def test_error() -> None:
    """Test to compare characters tables about Windows file system."""
    error_table: Strs = GroupedCharacters().get_error_table()

    _compare_count(9, error_table)
    _compare_both_ends(["\\", "|"], error_table)
