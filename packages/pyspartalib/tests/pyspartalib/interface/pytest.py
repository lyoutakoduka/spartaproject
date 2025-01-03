#!/usr/bin/env python

"""Interface module of "pytest".

Separate pure python code and other.
"""

import pytest

fail = pytest.fail
raises = pytest.raises

__all__ = ["fail", "raises"]
