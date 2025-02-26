#!/usr/bin/env python

"""User defined types about callable object."""

from collections.abc import Callable

Func = Callable[[], None]
IntStrFunc = Callable[[int], str | None]
