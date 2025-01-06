#!/usr/bin/env python

from collections.abc import Callable

from pyspartalib.context.type_context import Param, Type
from pyspartalib.script.decorator_generator import TransferFunction

Func = Callable[[], None]


class TemporaryDecorator(TransferFunction):
    def __init__(self, text: str | None = None) -> None:
        if text is None:
            text = ""

        self.text = text

    def wrapper(
        self,
        function: Callable[Param, Type],
        *arguments: Param.args,
        **key_arguments: Param.kwargs,
    ) -> Type:
        result: Type = function(*arguments, **key_arguments)
        self.text *= 2
        return result

    def show(self) -> str:
        return self.text


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _decorate_function(test_instance: TemporaryDecorator) -> Func:
    @test_instance.decorator
    def text_print() -> None:
        """Text doc."""

    text_print()

    return text_print


def test_name() -> None:
    test_instance = TemporaryDecorator()

    text_print: Func = _decorate_function(test_instance)

    _difference_error(text_print.__name__, "text_print")


def test_doc() -> None:
    test_instance = TemporaryDecorator()

    text_print: Func = _decorate_function(test_instance)

    _difference_error(text_print.__doc__, "Text doc.")


def test_text() -> None:
    message: str = "Hello!"
    test_instance = TemporaryDecorator(message)

    _decorate_function(test_instance)

    _difference_error(test_instance.show(), "Hello!Hello!")
