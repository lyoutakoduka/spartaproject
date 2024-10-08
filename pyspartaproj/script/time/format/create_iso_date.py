#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs, Strs2


def _get_groups() -> Strs:
    return ["year", "hour", "zone"]


def _get_types_year() -> Strs:
    return ["year", "month", "day"]


def _get_types_hour() -> Strs:
    return ["hour", "minute", "second"]


def _get_types_zone() -> Strs:
    return ["hour", "minute"]


def _get_types() -> Strs2:
    return [_get_types_year(), _get_types_hour(), _get_types_zone()]
