#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.filter_table import FilterTable


def _filter_text(texts: Strs, filter_table: FilterTable) -> bool:
    return filter_table.contain("".join(texts))


def _enable_text(texts: Strs, filter_table: FilterTable) -> None:
    assert _filter_text(texts, filter_table)


def _disable_text(texts: Strs, filter_table: FilterTable) -> None:
    assert not _filter_text(texts, filter_table)


def _get_zero(multiple: bool = False) -> str:
    return "\uff10" if multiple else "0"


def test_ascii() -> None:
    _enable_text(["A", "a", _get_zero()], FilterTable())


def test_other() -> None:
    _disable_text(["À", "à", _get_zero()], FilterTable())


def test_multiple() -> None:
    _enable_text(
        ["\uff21", "\uff41", _get_zero(multiple=True)],
        FilterTable(multiple=True),
    )
