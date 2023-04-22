#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable, TypeVar, ParamSpec
from functools import wraps

_R = TypeVar('_R')
_P = ParamSpec('_P')


class TransferFunc:
    def wrapper(self, func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
        return func(*args, **kwargs)

    def deco(self, func: Callable[_P, _R]) -> Callable[_P, _R]:
        @wraps(func)
        def register_func(*args: _P.args, **kwargs: _P.kwargs) -> _R:
            return self.wrapper(func, *args, **kwargs)
        return register_func
