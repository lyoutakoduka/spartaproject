#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable, TypeVar, ParamSpec

from scripts.deco_generator import TransferFunc

_R = TypeVar('_R')
_P = ParamSpec('_P')


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
