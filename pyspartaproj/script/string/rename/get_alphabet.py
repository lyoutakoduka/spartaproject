#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.integer_context import Ints


def _fill_character(characters: Ints) -> Ints:
    return list(range(characters[0], characters[1] + 1))
