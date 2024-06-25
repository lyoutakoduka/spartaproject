#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs2


def _compare_counts(tables: Strs2) -> None:
    assert [26, 26, 10, 33] == [len(table) for table in tables]
