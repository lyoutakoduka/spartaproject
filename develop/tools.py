#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import functools
from typing import Callable


def sandwich(count: int = 79):
    def _decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            def _line(id: str):
                print(id * count)

            _line('.')
            result = func(*args, **kwargs)
            _line('-')

            return result
        return _wrapper
    return _decorator


def _main() -> bool:
    MESSAGE: str = "Hello, World!"

    @sandwich()
    def _messages_sand():
        print(MESSAGE)

    _messages_sand()

    return True


if __name__ == '__main__':
    sys.exit(_main())
