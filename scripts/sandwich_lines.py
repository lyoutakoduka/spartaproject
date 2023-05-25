#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.callable_context import CP, CR, Callable
from scripts.decorator_generator import TransferFunc


class SandWich(TransferFunc):
    def __init__(
        self, count: int = 79, begin: str = '.', end: str = '-',
    ) -> None:
        self._count = count
        self._begin = begin
        self._end = end

    def wrapper(
        self,
        function: Callable[CP, CR],
        *arguments: CP.args,
        **key_arguments: CP.kwargs,
    ) -> CR:
        def line(id: str) -> None:
            print(id * self._count)

        line(self._begin)
        result: CR = function(*arguments, **key_arguments)
        line(self._end)

        return result
