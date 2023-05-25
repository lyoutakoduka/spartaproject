#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.callable_context import CP, CR, Callable
from scripts.decorator_generator import TransferFunc


class TestDeco(TransferFunc):
    def __init__(self, text: str = '') -> None:
        self.text = text

    def wrapper(
        self, function: Callable[CP, CR], *args: CP.args, **kwargs: CP.kwargs,
    ) -> CR:
        result: CR = function(*args, **kwargs)
        self.text *= 2
        return result

    def show(self) -> str:
        return self.text


def test_name() -> None:
    test_deco = TestDeco()

    @test_deco.decorator
    def text_print() -> None: pass
    text_print()

    EXPECTED_FUNCTION: str = 'text_print'
    assert EXPECTED_FUNCTION == text_print.__name__


def test_doc() -> None:
    test_deco = TestDeco()

    @test_deco.decorator
    def text_print() -> None:
        """text doc"""
        pass
    text_print()

    EXPECTED_DOC: str = 'text doc'
    assert EXPECTED_DOC == text_print.__doc__


def test_text() -> None:
    MESSAGE: str = "Hello!"
    test_deco = TestDeco(MESSAGE)

    @test_deco.decorator
    def text_print() -> None: pass
    text_print()

    EXPECTED_TEXT: str = 'Hello!Hello!'
    assert EXPECTED_TEXT == test_deco.show()


def main() -> bool:
    test_name()
    test_doc()
    test_text()
    return True
