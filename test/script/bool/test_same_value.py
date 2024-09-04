#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.bool_context import BoolPair, Bools
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.bool.same_value import bool_same_array, bool_same_pair


def _confirm(status: bool) -> None:
    assert status


def _confirm_error(status: bool) -> None:
    assert not status


def _expected_list(status: bool) -> Bools:
    return [status] * 3


def _expected_keys() -> Strs:
    return ["R", "G", "B"]


def _expected_pair(status: bool) -> BoolPair:
    return {
        key: value
        for key, value in zip(_expected_keys(), _expected_list(status))
    }


def test_empty() -> None:
    _confirm_error(bool_same_array([]))


def test_mixed() -> None:
    _confirm_error(bool_same_array([False, True, False]))


def test_false() -> None:
    _confirm_error(bool_same_array(_expected_list(False)))


def test_array() -> None:
    _confirm(bool_same_array(_expected_list(True)))


def test_invert() -> None:
    _confirm(bool_same_array(_expected_list(False), invert=True))


def test_pair() -> None:
    _confirm(bool_same_pair(_expected_pair(True)))


def test_pair_invert() -> None:
    _confirm(bool_same_pair(_expected_pair(False), invert=True))
