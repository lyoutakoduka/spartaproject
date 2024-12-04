#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle I/O functionalities of any script called pipeline."""

from decimal import Decimal

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.project.log_pipeline import LogPipeline
from pyspartaproj.script.string.off_stdout import StdoutText


def _get_interval() -> Decimal:
    return Decimal("0.3")


def _get_message() -> str:
    return "test"


def _get_timer_log(interval: str, messages: str) -> str:
    return interval + "s" + ": " + messages


def _get_expected() -> str:
    return _get_timer_log(str(_get_interval()), _get_message())


def _get_expected_print() -> str:
    return _get_expected() + "\n"


def _show_log(messages: Strs, pipeline: LogPipeline) -> None:
    pipeline.show_log(messages, force=True)


def _convert_log(messages: Strs, pipeline: LogPipeline) -> str:
    stdout_text = StdoutText()

    @stdout_text.decorator
    def _messages() -> None:
        _show_log(messages, pipeline)

    _messages()

    return stdout_text.show()


def _get_result(pipeline: LogPipeline) -> str:
    return _convert_log([_get_message()], pipeline)


def _get_result_text(pipeline: LogPipeline) -> str:
    if logs := pipeline.get_log():
        return logs[0]
    else:
        fail()


def _create_pipeline() -> LogPipeline:
    return LogPipeline()


def _create_pipeline_text() -> LogPipeline:
    return LogPipeline(disable_shown=True)


def _initialize_pipeline(pipeline: LogPipeline) -> LogPipeline:
    pipeline.restart(override=True, timer_interval=_get_interval())
    pipeline.increase_timer()

    return pipeline


def _compare_text(expected: str, result: str) -> None:
    assert expected == result


def test_print() -> None:
    """Test to show message as log to stdout."""
    _compare_text(
        _get_expected_print(),
        _get_result(_initialize_pipeline(_create_pipeline())),
    )
