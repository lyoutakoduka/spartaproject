#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for test to execute specific script in Python."""


def _main() -> None:
    for i in range(3):
        print(str(i).zfill(3))


if __name__ == "__main__":
    _main()
