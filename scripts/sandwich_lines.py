#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable, TypeVar, ParamSpec
from functools import wraps

from scripts.deco_generator import TransferFunc

_R = TypeVar('_R')
_P = ParamSpec('_P')


def sandwich(count: int = 79, begin: str = '.', end: str = '-'):
    def _decorator(func: Callable[_P, _R]) -> Callable[_P, _R]:

        @wraps(func)
        def _wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
            def _line(id: str) -> None:
                print(id * count)

            _line(begin)
            result = func(*args, **kwargs)
            _line(end)

            return result
        return _wrapper
    return _decorator


class SandWich(TransferFunc):
    def __init__(self, count: int = 79, begin: str = '.', end: str = '-') -> None:
        self._count = count
        self._begin = begin
        self._end = end

    def wrapper(self, func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
        def line(id: str) -> None:
            print(id * self._count)

        line(self._begin)
        result: _R = func(*args, **kwargs)
        line(self._end)

        return result
