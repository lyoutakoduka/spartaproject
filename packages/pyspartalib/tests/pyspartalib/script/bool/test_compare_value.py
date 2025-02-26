#!/usr/bin/env python

import pytest
from pyspartalib.script.bool.compare_value import (
    bool_compare_array,
    bool_compare_pair,
)


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def test_size() -> None:
    with pytest.raises(ValueError, match="size"):
        bool_compare_array([True], [True, False])


def test_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        bool_compare_array([], [])


def test_key() -> None:
    with pytest.raises(ValueError, match="unmatch"):
        bool_compare_pair(
            {"R": False, "G": True, "B": True},
            {"R": True, "error": False, "B": True},
        )


def test_array() -> None:
    _fail_error(bool_compare_array([True, False], [True, False]))


def test_pair() -> None:
    _fail_error(
        bool_compare_pair(
            {"R": True, "G": False, "B": True},
            {"R": True, "G": False, "B": True},
        ),
    )
