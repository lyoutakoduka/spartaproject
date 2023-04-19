#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

from scripts.same_elements import all_true


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


class TestDeco(TransferFunc):
    def __init__(self, text: str) -> None:
        self.text = text

    def wrapper(self, func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
        result: _R = func(*args, **kwargs)
        self.text *= 2
        return result

    def show(self) -> str:
        return self.text


def main() -> bool:
    MESSAGE: str = "Hello!"

    EXPECTED_FUNC: str = 'text_print'
    EXPECTED_DOC: str = 'text doc'
    EXPECTED_TEXT: str = 'Hello!Hello!'

    test_deco = TestDeco(MESSAGE)

    @test_deco.deco
    def text_print(text: str) -> bool:
        """text doc"""
        return True

    result: bool = all_true([
        text_print(MESSAGE),
        EXPECTED_FUNC == text_print.__name__,
        EXPECTED_DOC == text_print.__doc__,
        EXPECTED_TEXT == test_deco.show(),
    ])

    return result


if __name__ == '__main__':
    sys.exit(not main())
