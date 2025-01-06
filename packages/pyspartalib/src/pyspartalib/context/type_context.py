#!/usr/bin/env python

"""User defined types about callable object."""

from collections.abc import Callable
from typing import ParamSpec, TypeVar

Type = TypeVar("Type")
Param = ParamSpec("Param")
Func = Callable[[], None]
