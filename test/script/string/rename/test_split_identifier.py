#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.rename.split_identifier import SplitIdentifier


def test_path() -> None:
    split_identifier = SplitIdentifier()
    assert "_" == split_identifier.get_identifier()


def test_specific() -> None:
    identifier: str = "-"
    split_identifier = SplitIdentifier(identifier=identifier)
    assert identifier == split_identifier.get_identifier()
