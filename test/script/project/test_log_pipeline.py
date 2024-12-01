#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal


def _get_interval() -> Decimal:
    return Decimal("0.3")


def _get_message() -> str:
    return "test"


def _get_timer_log(interval: str, messages: str) -> str:
    return interval + "s" + ": " + messages + "\n"
