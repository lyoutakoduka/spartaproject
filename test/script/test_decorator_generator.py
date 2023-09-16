#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.callable_context import CP, CR, Callable
from script.decorator_generator import TransferFunction


class TemporaryDecorator(TransferFunction):
    def __init__(self, text: str = '') -> None:
        self.text = text

    def wrapper(
        self,
        function: Callable[CP, CR],
        *arguments: CP.args,
        **key_arguments: CP.kwargs
    ) -> CR:
        result: CR = function(*arguments, **key_arguments)
        self.text *= 2
        return result

    def show(self) -> str:
        return self.text


def test_name() -> None:
    test_instance = TemporaryDecorator()

    @test_instance.decorator
    def text_print() -> None: pass
    text_print()

    EXPECTED_FUNCTION: str = 'text_print'
    assert EXPECTED_FUNCTION == text_print.__name__


def test_doc() -> None:
    test_instance = TemporaryDecorator()

    @test_instance.decorator
    def text_print() -> None:
        """text doc"""
        pass
    text_print()

    EXPECTED_DOC: str = 'text doc'
    assert EXPECTED_DOC == text_print.__doc__


def test_text() -> None:
    MESSAGE: str = "Hello!"
    test_instance = TemporaryDecorator(MESSAGE)

    @test_instance.decorator
    def text_print() -> None: pass
    text_print()

    EXPECTED_TEXT: str = 'Hello!Hello!'
    assert EXPECTED_TEXT == test_instance.show()


def main() -> bool:
    test_name()
    test_doc()
    test_text()
    return True
