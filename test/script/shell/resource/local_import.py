#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import path


def _main() -> None:
    for text in path:
        print(text)


if __name__ == "__main__":
    _main()
