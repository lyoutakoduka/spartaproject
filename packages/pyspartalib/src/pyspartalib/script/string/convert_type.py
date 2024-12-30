#!/usr/bin/env python

"""Module to convert text to specific type."""


def convert_integer(index: str) -> int | None:
    """Convert text to type "integer".

    Args:
        index (str): Text you want to convert.

    Returns:
        int | None: Converted index from text.
    """
    try:
        return int(index)
    except BaseException:
        return None
