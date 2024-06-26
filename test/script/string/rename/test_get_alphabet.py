#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs2
from pyspartaproj.context.typed.user_context import Alphabets


def _compare_counts(tables: Strs2) -> None:
    assert [26, 26, 10, 33] == [len(table) for table in tables]


def _compare_filtered(expected: Strs2, tables: Strs2) -> None:
    assert expected == [[table[-i] for i in range(2)] for table in tables]


def _get_tables(result: Alphabets) -> Strs2:
    return [result["big"], result["small"], result["number"], result["other"]]
