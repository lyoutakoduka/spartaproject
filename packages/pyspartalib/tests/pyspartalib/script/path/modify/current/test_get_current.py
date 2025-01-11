#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get current working directory."""

from pyspartalib.script.path.modify.current.get_current import get_current


def test_current() -> None:
    """Test to cet current working directory."""
    assert get_current().exists()
