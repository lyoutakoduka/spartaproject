#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wrapper module to separate pure python code and other.

win32com: pywin32
"""

from win32com.client.dynamic import CDispatch  # noqa: F401 # type: ignore
