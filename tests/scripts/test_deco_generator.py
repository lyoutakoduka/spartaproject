#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable, TypeVar, ParamSpec

from scripts.deco_generator import TransferFunc


_R = TypeVar('_R')
_P = ParamSpec('_P')


class TestDeco(TransferFunc):
    def __init__(self, text: str = '') -> None:
        self.text = text

    def wrapper(self, func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
        result: _R = func(*args, **kwargs)
        self.text *= 2
        return result

    def show(self) -> str:
        return self.text


def test_name() -> None:
    test_deco = TestDeco()

    @test_deco.deco
    def text_print() -> None: pass
    text_print()

    EXPECTED_FUNC: str = 'text_print'
    assert EXPECTED_FUNC == text_print.__name__


def test_doc() -> None:
    test_deco = TestDeco()

    @test_deco.deco
    def text_print() -> None:
        """text doc"""
        pass
    text_print()

    EXPECTED_DOC: str = 'text doc'
    assert EXPECTED_DOC == text_print.__doc__


def test_text() -> None:
    MESSAGE: str = "Hello!"
    test_deco = TestDeco(MESSAGE)

    @test_deco.deco
    def text_print() -> None: pass
    text_print()

    EXPECTED_TEXT: str = 'Hello!Hello!'
    assert EXPECTED_TEXT == test_deco.show()


def main() -> bool:
    test_name()
    test_doc()
    test_text()
    return True
