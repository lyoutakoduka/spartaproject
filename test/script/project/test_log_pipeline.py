#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.project.log_pipeline import LogPipeline
from pyspartaproj.script.string.off_stdout import StdoutText


def _get_interval() -> Decimal:
    return Decimal("0.3")


def _get_message() -> str:
    return "test"


def _get_timer_log(interval: str, messages: str) -> str:
    return interval + "s" + ": " + messages + "\n"


def _get_expected() -> str:
    return _get_timer_log(str(_get_interval()), _get_message())


def _convert_log(messages: Strs, pipeline: LogPipeline) -> str:
    stdout_text = StdoutText()

    @stdout_text.decorator
    def _messages() -> None:
        pipeline.show_log(messages, force=True)

    _messages()

    return stdout_text.show()
