#!/usr/bin/env python
# -*- coding: utf-8 -*-

from platform import uname


def get_platform() -> str:
    return uname().system.lower()
