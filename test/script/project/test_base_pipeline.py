#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handling I/O functionality of any script called pipeline."""

from decimal import Decimal
from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.project.base_pipeline import BasePipeline
from pyspartaproj.script.string.off_stdout import StdoutText


def _get_config_file() -> Path:
    return get_resource(local_path=Path("base_pipeline", "forward.json"))


def _convert_print(messages: Strs, pipeline: BasePipeline) -> str:
    stdout_text = StdoutText()

    @stdout_text.decorator
    def _messages() -> None:
        pipeline.show_log(messages)

    _messages()

    return stdout_text.show()


def _read_path(pipeline: BasePipeline) -> Strs:
    path_context: PathPair = pipeline.get_path_context("test")
    return list(Path(path_context["print.path"]).parts)


def _create_pipeline(interval: str) -> BasePipeline:
    pipeline = BasePipeline(forward=_get_config_file())

    pipeline.restart(override=True, timer_interval=Decimal(interval))
    pipeline.increase_timer()

    return pipeline


def test_print() -> None:
    """Test ot show message as log to stdout."""
    interval: str = "0.3"
    expected: str = (
        interval + "s" + ": " + " ".join(["root", "body", "head"]) + "\n"
    )
    pipeline: BasePipeline = _create_pipeline(interval)

    assert expected == _convert_print(_read_path(pipeline), pipeline)
