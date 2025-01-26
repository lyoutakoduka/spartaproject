#!/usr/bin/env python

"""Test Module to get characters constructed by multiple or single byte."""

from collections.abc import Sized
from typing import get_type_hints

from pyspartalib.context.default.string_context import Strs, Strs2
from pyspartalib.context.type_context import Type
from pyspartalib.script.string.table.context.table_context import (
    CharacterTable,
)
from pyspartalib.script.string.table.grouped_table import GroupedTable


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _length_error(result: Sized, expected: int) -> None:
    if len(result) != expected:
        raise ValueError


def _get_expected_single() -> Strs2:
    return [["A", "Z"], ["a", "z"], ["0", "9"], [" ", "~"]]


def _get_expected_multiple() -> Strs2:
    return [
        ["\uff21", "\uff3a"],
        ["\uff41", "\uff5a"],
        ["\uff10", "\uff19"],
        ["\u3000", "\uff5e"],
    ]


def _compare_counts(tables: Strs2) -> None:
    for count, table in zip([26, 26, 10, 47], tables, strict=True):
        _length_error(table, count)


def _compare_both_ends(both_ends: Strs, table: Strs) -> None:
    _difference_error([table[-i] for i in range(2)], both_ends)


def _compare_filtered(expected: Strs2, tables: Strs2) -> None:
    for both_ends, table in zip(expected, tables, strict=True):
        _compare_both_ends(both_ends, table)


def _compare_size(result: CharacterTable) -> None:
    _length_error(list(get_type_hints(result).keys()), 4)


def _get_tables(table: CharacterTable) -> Strs2:
    return [table["upper"], table["lower"], table["number"], table["other"]]


def _compare_table(expected: Strs2, result: CharacterTable) -> None:
    _compare_size(result)

    tables: Strs2 = _get_tables(result)

    _compare_counts(tables)
    _compare_filtered(expected, tables)


def _compare_merged(table: CharacterTable, merged: Strs2) -> None:
    _difference_error(_get_tables(table), merged)


def test_single() -> None:
    """Test to get characters constructed by single byte."""
    _compare_table(
        _get_expected_single(),
        GroupedTable().get_table(),
    )


def test_multiple() -> None:
    """Test to get characters constructed by multiple byte."""
    _compare_table(
        _get_expected_multiple(),
        GroupedTable(multiple=True).get_table(),
    )


def test_merge() -> None:
    """Test to compare merged character tables and originals."""
    grouped_characters = GroupedTable()

    _compare_merged(
        grouped_characters.get_table(),
        grouped_characters.get_merged_tables(),
    )


def test_error() -> None:
    """Test to compare characters tables about Windows file system."""
    error_table: Strs = GroupedTable().get_error_table()

    _length_error(error_table, 9)
    _compare_both_ends(["\\", "|"], error_table)
