#!/usr/bin/env python

"""Module to confirm that type bool values are same and True."""

from pyspartalib.context.default.bool_context import BoolPair, Bools


def bool_same_array(flags: Bools, invert: bool = False) -> bool:
    """Confirm that list of bool value are same and True.

    Args:
        flags (Bools): List of bool value you want to check.

        invert (bool, optional): Defaults to False.
            False: Return True if all Values are True.
            True: Return True if all Values are False.

    Returns:
        bool: True if values are same.

    """
    if 0 == len(flags):
        return False

    flags = list(set(flags))

    if 1 != len(flags):
        return False

    if not invert ^ flags[0]:
        return False

    return True


def bool_same_pair(flag_pair: BoolPair, invert: bool = False) -> bool:
    """Confirm that pair of bool value are same and True.

    Args:
        flag_pair (BoolPair): Pair of bool value you want to check.

        invert (bool, optional): Defaults to False.
            False: Return True if all Values are True.
            True: Return True if all Values are False.
            It's used for argument "invert" of function "bool_same_array".

    Returns:
        bool: True if values are same.

    """
    return bool_same_array(
        [value for value in flag_pair.values()], invert=invert
    )
