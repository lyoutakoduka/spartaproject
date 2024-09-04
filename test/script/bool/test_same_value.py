#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.bool.same_value import bool_same_array, bool_same_pair


def _confirm(status: bool) -> None:
    assert status


def confirm_error(status: bool) -> None:
    assert not status


def test_empty() -> None:
    confirm_error(bool_same_array([]))


def test_mixed() -> None:
    confirm_error(bool_same_array([False, True, False]))


def test_false() -> None:
    confirm_error(bool_same_array([False, False, False]))


def test_array() -> None:
    _confirm(bool_same_array([True, True, True]))


def test_invert() -> None:
    _confirm(bool_same_array([False, False, False], invert=True))


def test_pair() -> None:
    _confirm(bool_same_pair({"R": True, "G": True, "B": True}))


def test_pair_invert() -> None:
    _confirm(bool_same_pair({"R": False, "G": False, "B": False}, invert=True))
