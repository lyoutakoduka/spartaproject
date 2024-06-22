#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import Ints, Ints3


def _fill_character(characters: Ints) -> Ints:
    return list(range(characters[0], characters[1] + 1))


def _get_hex_tables() -> Ints3:
    return [
        [[0xFF21, 0xFF3A], [0x41, 0x5A]],
        [[0xFF41, 0xFF5A], [0x61, 0x7A]],
        [[0xFF10, 0xFF19], [0x30, 0x39]],
    ]
