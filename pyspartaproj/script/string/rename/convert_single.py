#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert multiple byte characters to single byte characters."""

from pyspartaproj.context.default.integer_context import Ints, Ints3
from pyspartaproj.context.default.string_context import (
    StrPair,
    Strs,
    Strs2,
    Strs3,
    Trans,
)
from pyspartaproj.context.typed.user_context import CharacterTable
from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class ConvertSingle:
    """Class to convert multiple byte characters to single byte."""

    def _fill_character(self, characters: Ints) -> Ints:
        return list(range(characters[0], characters[1] + 1))

    def _get_hex_tables(self) -> Ints3:
        return [
            [[0xFF21, 0xFF3A], [0x41, 0x5A]],
            [[0xFF41, 0xFF5A], [0x61, 0x7A]],
            [[0xFF10, 0xFF19], [0x30, 0x39]],
        ]

    def _fill_hex_tables(self, hex_tables: Ints3) -> Ints3:
        return [
            [self._fill_character(hex_span) for hex_span in hex_table]
            for hex_table in hex_tables
        ]

    def _to_characters(self, numbers: Ints) -> Strs:
        return [chr(number) for number in numbers]

    def _get_translate_table(self, filled_tables: Ints3) -> StrPair:
        return dict(
            [
                self._to_characters(list(numbers))
                for filled_table in filled_tables
                for numbers in zip(filled_table[0], filled_table[1])
            ]
        )

    def _get_merged_tables(self, table: CharacterTable) -> Strs2:
        return [table["big"], table["small"], table["number"], table["other"]]

    def _get_tables_pair(self) -> Strs3:
        return [
            self._get_merged_tables(
                GroupedCharacters(multiple=(0 == i)).get_table()
            )
            for i in range(2)
        ]

    def _get_link_table(self, tables_pair: Strs3) -> StrPair:
        return {
            big: small
            for big_table, small_table in zip(tables_pair[0], tables_pair[1])
            for big, small in zip(big_table, small_table)
        }

    def convert(self, text: str) -> str:
        """Convert multiple byte characters to single byte characters.

        Args:
            text (str): String which might include multiple byte characters.

        Returns:
            str: Converted single byte characters.
        """
        translated: Trans = str.maketrans(  # Type Trans is necessary.
            self._get_translate_table(
                self._fill_hex_tables(self._get_hex_tables())
            )
        )
        return text.translate(translated)
