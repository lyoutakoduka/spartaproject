#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script to execute Python module to get Python version on server."""


from sys import version


def _main() -> None:
    print(version)


if __name__ == "__main__":
    _main()
