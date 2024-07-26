#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get character tables constructed by multiple or single byte."""

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs, Strs2, StrsPair
from pyspartaproj.context.typed.user_context import CharacterTable


class GroupedCharacters:
    """Class to get character tables constructed by multiple or single byte."""

    def _get_index_base(self, multiple: bool) -> int:
        index_base: int = 33

        if multiple:
            index_base += 65248

        return index_base

    def _get_special_pair(self) -> StrsPair:
        return {
            " ": ["\u3000"],
            ".": ["\u30fb", "\u3002", "\u2026"],
            ",": ["\u3001"],
            "[": ["\u300c", "\u3010", "\u300e"],
            "]": ["\u300d", "\u3011", "\u300f"],
            '"': ["\u201d", "\u201c"],
            "'": ["\u2019", "\u2018"],
        }

    def _get_special_tables(self, multiple: bool) -> Strs:
        return [
            key if multiple else value
            for key, values in self._get_special_pair().items()
            for value in values
        ]

    def _initialize_variables(self, multiple: bool) -> None:
        self._index_base: int = self._get_index_base(multiple)
        self._special_tables: Strs = self._get_special_tables(multiple)

    def _struct_character_table(
        self, upper: Strs, lower: Strs, number: Strs, other: Strs
    ) -> CharacterTable:
        return {
            "upper": upper,
            "lower": lower,
            "number": number,
            "other": other,
        }

    def _create_character_table(self, index: int, span: int) -> Strs:
        return [chr(index + i) for i in range(span)]

    def _get_indices_begin(self, indices_span: Ints) -> Ints:
        indices_begin: Ints = []
        index_begin: int = 0

        for i in range(len(indices_span)):
            index_begin += 0 if 0 == i else indices_span[i - 1]
            indices_begin += [index_begin]

        return indices_begin

    def _create_character_tables(self) -> Strs2:
        indices_span: Ints = [15, 10, 7, 26, 6, 26, 4]

        return [
            self._create_character_table(begin + self._index_base, span)
            for begin, span in zip(
                self._get_indices_begin(indices_span), indices_span
            )
        ]

    def _merge_string_tables(
        self, indices: Ints, character_tables: Strs2
    ) -> Strs:
        merged_table: Strs = []

        for index in indices:
            merged_table += character_tables[index]

        return merged_table

    def _get_other_table(self, character_tables: Strs2) -> Strs:
        return self._merge_string_tables([0, 2, 4, 6], character_tables)

    def _restructure_tables(self, character_tables: Strs2) -> CharacterTable:
        return self._struct_character_table(
            character_tables[3],
            character_tables[5],
            character_tables[1],
            self._special_tables + self._get_other_table(character_tables),
        )

    def get_table(self) -> CharacterTable:
        """Get character tables constructed by multiple or single byte.

        The character tables include following 4 types characters.

        1. Upper case letters: "A" - "Z"

        2. Lower case letters: "a" - "z"

        3. Numbers: "0" - "9"

        4. Other characters: e.g., " ", "!", and "~".
            Characters other than upper and lower case letters
                and numbers in Ascii table.

        If tables including multiple byte character is returned,
            there are selected from Unicode table corresponds to Ascii table.

        Returns:
            CharacterTable: Character tables.
        """
        return self._restructure_tables(self._create_character_tables())

    def get_merged_tables(self) -> Strs2:
        """Get merged character tables.

        It's include all attributes in the class about character table.

        Returns:
            Strs2: Character tables listed by default order.
        """
        table: CharacterTable = self.get_table()
        return [
            table["upper"],
            table["lower"],
            table["number"],
            table["other"],
        ]

    def __init__(self, multiple: bool = False) -> None:
        """Initialize variables in class.

        Args:
            multiple (bool, optional): Defaults to False.
                True if you want to select character tables
                    which is constructed by multiple byte.
        """
        self._initialize_variables(multiple)
