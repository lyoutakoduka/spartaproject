#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs2
from pyspartaproj.context.typed.user_context import Alphabets
from pyspartaproj.script.string.rename.get_alphabet import get_alphabet


def _compare_counts(tables: Strs2) -> None:
    assert [26, 26, 10, 33] == [len(table) for table in tables]


def _compare_filtered(expected: Strs2, tables: Strs2) -> None:
    assert expected == [[table[-i] for i in range(2)] for table in tables]


def _compare_size(result: Alphabets) -> None:
    assert 4 == len(result)


def _get_tables(result: Alphabets) -> Strs2:
    return [result["big"], result["small"], result["number"], result["other"]]


def _common_test(expected: Strs2, result: Alphabets) -> None:
    _compare_size(result)

    tables: Strs2 = _get_tables(result)

    _compare_counts(tables)
    _compare_filtered(expected, tables)


def test_single() -> None:
    _common_test(
        [["A", "Z"], ["a", "z"], ["0", "9"], [" ", "~"]], get_alphabet()
    )


def test_multiple() -> None:
    _common_test(
        [
            ["\uff21", "\uff3a"],
            ["\uff41", "\uff5a"],
            ["\uff10", "\uff19"],
            ["\u3000", "\uff5e"],
        ],
        get_alphabet(multiple=True),
    )
