#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to show simple numbers as string type for module test."""

from pyspartalib.context.default.string_context import Strs


def temporary_text(count: int, digit: int) -> Strs:
    """Function to show simple numbers as string.

    Args:
        count (int): Count of numbers which is start from zero.

        digit (int): Digit of numbers as string type which is filled by zero.

        e.g., following text is shown if "count" is 3, and "digit" is 4.

        0000
        0001
        0002

    Returns:
        Strs: Numbers as string type which is filled by zero.

    """
    return [str(i).zfill(digit) for i in range(count)]
