#!/usr/bin/env python

from os import getenv


def _get_environment(key: str) -> bool:
    return getenv(key.upper()) is not None
