#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs


def _get_groups() -> Strs:
    return ["year", "hour", "zone"]


def _get_types_year() -> Strs:
    return ["year", "month", "day"]


def _get_types_hour() -> Strs:
    return ["hour", "minute", "second"]
