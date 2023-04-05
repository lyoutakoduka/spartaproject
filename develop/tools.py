#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from typing import List, Dict, Union, Callable


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


def formatting(asset: Union[List[str], Dict[str, str]]) -> str:
    if isinstance(asset, Dict):
        sorted_asset = sorted(asset.items())
        PAIR = ': '
        asset = [PAIR.join(item) for item in sorted_asset]

    ENTER = '\n'
    message = ENTER.join(asset)

    return message


def __main():
    orders = ['first', 'second', 'third']
    animals = {'dog': 'bow', 'cat': 'mew'}
    assets = [orders, animals]

    @sandwich()
    def messages_sand():
        for asset in assets:
            message = formatting(asset)
            print(message)

    messages_sand()


if __name__ == '__main__':
    __main()
