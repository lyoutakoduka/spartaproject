#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

from scripts.off_stdout import stdout_to_text, StdResults


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


def main() -> bool:
    MESSAGE: str = "Hello, World!"
    RESULT: str = \
        '-------------\n' \
        'Hello, World!\n' \
        '=============\n'

    results = StdResults()

    @stdout_to_text(results)
    @sandwich(len(MESSAGE), '-', '=')
    def _messages_sand() -> None:
        print(MESSAGE)

    _messages_sand()

    return RESULT == results.stdout


if __name__ == '__main__':
    sys.exit(not main())
