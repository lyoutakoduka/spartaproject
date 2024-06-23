#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import Ints, Ints2
from pyspartaproj.context.default.string_context import Strs, Strs2


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
