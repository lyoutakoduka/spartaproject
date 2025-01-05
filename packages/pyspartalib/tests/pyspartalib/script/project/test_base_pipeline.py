#!/usr/bin/env python

"""Test module to handle all functionalities of any script called pipeline."""

from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.project.base_pipeline import BasePipeline


def _strings_error(result: Strs, expected: Strs) -> None:
    if result != expected:
        raise ValueError


def _get_expected() -> Strs:
    return ["root", "body", "head"]


def _get_config_file() -> Path:
    return get_resource(local_path=Path("base_pipeline", "forward.json"))


def _get_path_context(pipeline: BasePipeline) -> PathPair:
    return pipeline.get_path_context("test")


def _get_path(pipeline: BasePipeline) -> Path:
    return _get_path_context(pipeline)["print.path"]


def _get_result(pipeline: BasePipeline) -> Strs:
    return list(Path(_get_path(pipeline)).parts)


def _create_pipeline() -> BasePipeline:
    return BasePipeline(forward=_get_config_file())


def _compare_text(expected: Strs, result: Strs) -> None:
    assert expected == result


def test_print() -> None:
    """Test to import strings from module outside."""
    _strings_error(_get_result(_create_pipeline()), _get_expected())
