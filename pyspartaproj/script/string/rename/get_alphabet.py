#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import Ints, Ints2
from pyspartaproj.context.default.string_context import Strs, Strs2
from pyspartaproj.context.typed.user_context import Alphabets


def _to_characters(numbers: Ints) -> Strs:
    return [chr(number) for number in numbers]


def _fill_character(characters: Ints) -> Ints:
    return list(range(characters[0], characters[1] + 1))


def _get_hex_tables(multiple: bool) -> Ints2:
    if multiple:
        return [[0xFF21, 0xFF3A], [0xFF41, 0xFF5A], [0xFF10, 0xFF19]]
    else:
        return [[0x41, 0x5A], [0x61, 0x7A], [0x30, 0x39]]


def _fill_hex_tables(hex_table: Ints2) -> Ints2:
    return [_fill_character(hex_span) for hex_span in hex_table]


def _get_alphabet_table(filled_table: Ints2) -> Strs2:
    return [_to_characters(numbers) for numbers in filled_table]


def _get_table(multiple: bool) -> Strs2:
    return _get_alphabet_table(_fill_hex_tables(_get_hex_tables(multiple)))


def _struct_alphabet(
    big: Strs, small: Strs, number: Strs, other: Strs
) -> Alphabets:
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
    indices_span: Ints = [16, 10, 7, 26, 6, 26, 4]

    return [
        _get_string_table(begin + index_base, span)
        for begin, span in zip(_get_indices_begin(indices_span), indices_span)
    ]


def _get_index_base(multiple: bool) -> int:
    index_base: int = 32

    if multiple:
        index_base += 65248

    return index_base


def _merge_string_tables(indices: Ints, alphabet_tables: Strs2) -> Strs:
    merged_table: Strs = []

    for index in indices:
        merged_table += alphabet_tables[index]

    return merged_table


def get_alphabet(multiple: bool = False) -> Alphabets:
    return _struct_alphabet(*_get_table(multiple))
