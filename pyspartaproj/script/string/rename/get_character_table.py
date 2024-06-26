#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs, Strs2
from pyspartaproj.context.typed.user_context import CharacterTable


def _struct_character_table(
    big: Strs, small: Strs, number: Strs, other: Strs
) -> CharacterTable:
    return {"big": big, "small": small, "number": number, "other": other}


def _get_string_table(index: int, span: int) -> Strs:
    return [chr(index + i) for i in range(span)]


def _get_indices_begin(indices_span: Ints) -> Ints:
    indices_begin: Ints = []
    index_begin: int = 0

    for i in range(len(indices_span)):
        index_begin += 0 if 0 == i else indices_span[i - 1]
        indices_begin += [index_begin]

    return indices_begin


def _get_string_tables(index_base: int) -> Strs2:
    indices_span: Ints = [15, 10, 7, 26, 6, 26, 4]

    return [
        _get_string_table(begin + index_base, span)
        for begin, span in zip(_get_indices_begin(indices_span), indices_span)
    ]


def _get_index_base(multiple: bool) -> int:
    index_base: int = 33

    if multiple:
        index_base += 65248

    return index_base


def _merge_string_tables(indices: Ints, alphabet_tables: Strs2) -> Strs:
    merged_table: Strs = []

    for index in indices:
        merged_table += alphabet_tables[index]

    return merged_table


def _get_special_tables(multiple: bool) -> Strs:
    return ["\u3000" if multiple else " "]


def _get_other_table(alphabet_tables: Strs2) -> Strs:
    return _merge_string_tables([0, 2, 4, 6], alphabet_tables)


def _restructure_tables(
    special_tables: Strs, alphabet_tables: Strs2
) -> CharacterTable:
    return _struct_character_table(
        alphabet_tables[3],
        alphabet_tables[5],
        alphabet_tables[1],
        special_tables + _get_other_table(alphabet_tables),
    )


def get_character_table(multiple: bool = False) -> CharacterTable:
    return _restructure_tables(
        _get_special_tables(multiple),
        _get_string_tables(_get_index_base(multiple)),
    )
