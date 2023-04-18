#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from contextlib import redirect_stdout
import tempfile
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

from scripts.format_texts import format_indent


_R = TypeVar('_R')
_P = ParamSpec('_P')


class StdResults:
    def set_stdout(self, text: str) -> None:
        self.stdout = text

    def __init__(self) -> None:
        self.set_stdout('')


def _outside_wrapper(results: StdResults, func: Callable[_P, _R]) -> Callable[_P, _R]:

    @wraps(func)
    def _wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        def _execute_func() -> _R:
            return func(*args, **kwargs)

        def _get_return(text: str) -> None:
            results.set_stdout(text)

        with tempfile.TemporaryDirectory() as tmp_directory:
            tmp_file_path: str = os.path.join(tmp_directory, 'tmp')

            with open(tmp_file_path, 'w') as file:
                with redirect_stdout(file):
                    result: _R = _execute_func()

            with open(tmp_file_path, 'r') as file:
                _get_return(file.read())

        return result
    return _wrapper


def stdout_to_text(results: StdResults):
    def _decorator(func: Callable[_P, _R]) -> Callable[_P, _R]:
        return _outside_wrapper(results, func)
    return _decorator


def main() -> bool:
    MESSAGE: str = "Hello, World!"
    EXPECTED: str = """
        Hello, World!
        Hello, World!
        """

    expected: str = format_indent(EXPECTED, stdout=True)

    results = StdResults()

    @stdout_to_text(results)
    def _messages() -> None:
        print(MESSAGE)
        print(MESSAGE)

    _messages()

    return expected == results.stdout


if __name__ == '__main__':
    sys.exit(not main())
