#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle I/O functionalities of any script called pipeline."""

from decimal import Decimal

from pyspartaproj.context.custom.log_context import LogFunc
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.project.log_pipeline import LogPipeline
from pyspartaproj.script.string.off_stdout import StdoutText


def _get_interval() -> Decimal:
    return Decimal("0.3")


def _get_interval_texts() -> Strs:
    return ["0.0"] + [str(_get_interval())] * 2


def _get_message() -> str:
    return "test"


def _get_messages() -> Strs:
    return [_get_message()]


def _get_message_texts() -> Strs:
    return ["begin", _get_message(), "end"]


def _get_timer_log(interval: str, messages: str) -> str:
    return interval + "s" + ": " + messages


def _get_expected_log() -> Strs:
    return [
        _get_timer_log(interval, message)
        for interval, message in zip(
            _get_interval_texts(), _get_message_texts()
        )
    ]


def _get_expected() -> str:
    return _get_timer_log(str(_get_interval()), _get_message())


def _get_expected_single() -> Strs:
    return [_get_expected()]


def _show_log(messages: Strs, pipeline: LogPipeline) -> LogPipeline:
    pipeline.show_log(messages, force=True)
    return pipeline


def _decorate_function(
    function: LogFunc, stdout_text: StdoutText
) -> StdoutText:
    @stdout_text.decorator
    def _messages() -> None:
        function()

    _messages()

    return stdout_text


def _execute_log_function(function: LogFunc) -> str:
    return _decorate_function(function, StdoutText()).show()


def _initialize_pipeline(pipeline: LogPipeline) -> None:
    pipeline.restart(override=True, timer_interval=_get_interval())
    pipeline.increase_timer()


def _start_pipeline(function: LogFunc) -> LogPipeline:
    pipeline: LogPipeline = function()
    _initialize_pipeline(pipeline)
    return pipeline


def _record_log(function: LogFunc) -> LogPipeline:
    return _show_log(_get_messages(), _start_pipeline(function))


def _record_log_single(function: LogFunc) -> LogPipeline:
    return _show_log(
        _get_messages(),
        _reset_stored_log(_start_pipeline(function)),
    )


def _wrapper_print(function: LogFunc) -> LogFunc:
    return lambda: _record_log(function)


def _get_result_print(function: LogFunc) -> Strs:
    return _execute_log_function(_wrapper_print(function)).splitlines()


def _find_log_error(logs: Strs | None) -> Strs:
    if logs is None:
        fail()

    return logs


def _get_log(pipeline: LogPipeline) -> Strs:
    return _find_log_error(pipeline.get_log())


def _reset_stored_log(pipeline: LogPipeline) -> LogPipeline:
    _get_log(pipeline)
    return pipeline


def _close_log(pipeline: LogPipeline) -> Strs:
    return _find_log_error(pipeline.close_log())


def _get_result_all(function: LogFunc) -> Strs:
    return _close_log(_record_log(function))


def _get_result_single(pipeline: LogPipeline) -> Strs:
    return _get_log(_show_log(_get_messages(), pipeline))


def _create_pipeline() -> LogPipeline:
    return LogPipeline()


def _create_pipeline_text() -> LogPipeline:
    return LogPipeline(disable_shown=True)


def _compare_text(expected: Strs, result: Strs) -> None:
    assert expected == result


def test_print() -> None:
    """Test to show log message to stdout."""
    _compare_text(_get_expected_log(), _get_result_print(_create_pipeline))


def test_all() -> None:
    _compare_text(_get_expected_log(), _get_result_all(_create_pipeline_text))


def test_single() -> None:
    """Test to get recorded log messages at all Together."""
    _compare_text(
        _get_expected_single(),
        _get_result_single(
            _reset_stored_log(_start_pipeline(_create_pipeline_text))
        ),
    )
