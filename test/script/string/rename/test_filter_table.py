#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.filter_table import FilterTable


def _filter_text(texts: Strs, filter_table: FilterTable) -> bool:
    return filter_table.contain("".join(texts))


def _enable_text(texts: Strs, filter_table: FilterTable) -> None:
    assert _filter_text(texts, filter_table)
