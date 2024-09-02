#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.bool_context import BoolPair, Bools


def bool_same_array(flags: Bools, invert: bool = False) -> bool:
    if 0 == len(flags):
        return False

    flags = list(set(flags))

    if 1 != len(flags):
        return False

    if not invert ^ flags[0]:
        return False

    return True


def bool_same_pair(flag_pair: BoolPair) -> bool:
    return bool_same_array([value for value in flag_pair.values()])
